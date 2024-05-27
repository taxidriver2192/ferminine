import json
import os
import uuid

# Path to the JSON file
json_file_path = "produkter/services.json"

# Output HTML file path
output_html_path = "produkter/services.html"

# Read the JSON data
with open(json_file_path, "r", encoding="utf-8") as json_file:
    categories_data = json.load(json_file)

# Function to ensure each service has a unique ID
def ensure_service_ids(categories):
    for category in categories:
        for service in category['services']:
            if 'service_id' not in service or not service['service_id']:
                service['service_id'] = str(uuid.uuid4())

# Ensure all services have unique IDs
ensure_service_ids(categories_data)

# Define image URLs for each category
image_urls = {
    "ANSIGTSBEHANDLINGER": "http://www.feminine.aveo19.dk/wp-content/uploads/woman-making-facial-treatment-in-a-beauty-saloon.jpg",
    "KROPSBEHANDLINGER": "http://www.feminine.aveo19.dk/wp-content/uploads/spa-massage-indian-woman-relaxing-on-table-while-therapist-massaging-her-shoulders.jpg",
    "VIPPE & BRYN BEHANDLINGER": "http://www.feminine.aveo19.dk/wp-content/uploads/IMG_1408.jpg",
    "LYCON VOKSBEHANDLINGER": "http://www.feminine.aveo19.dk/wp-content/uploads/liquid-sugar-wax-on-spatula-beige.jpg",
    "PAKKER": "http://www.feminine.aveo19.dk/wp-content/uploads/beauty-box-wellness-zero-waste-gift-natural-organic-spa-care-package-handmade-eco-box-mental.jpg"
}

# Start creating the HTML content
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Services</title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <style>
        .category, .service, .service-details {
            display: none;
        }
        .category.active, .service.active, .service-details.active {
            display: block;
        }
        .category-card, .service-card {
            cursor: pointer;
            transition: transform 0.3s;
        }
        .category-card:hover {
            transform: scale(1.01);
        }
        .category-banner, .service-banner {
            position: relative;
            text-align: center;
            color: white;
        }
        .category-card {
            background-size: cover;
            background-position: center;
            border-radius: 500px;
            width: 100%;
            height: 400px;
            margin: 0 auto;
        }
        .category-card .banner-text {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background-color: rgba(0, 0, 0, 0.5);
            padding: 10px;
            border-radius: 10px;
        }

        .service .service-banner,
        .service-details .service-banner{
            min-height: 200px;
            display: flex;
            justify-content: center;
            align-items: center;
            background-size: cover;
            background-position: center;
        }
        .category-banner .banner-text {
            background: none;
            padding: 0;
        }
        .category .banner-text {
            padding-top: 20px;
        }
        .category-card h5 {
            margin-top: 20px;
        }
        .service, 
        .service-details{
            width: 100%;
            text-align: left;
        }
        .category .banner-text h2 {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
            font-size: 15px;
            font-weight: 400;
            line-height: 22.5px;
            text-align: center;
            text-size-adjust: 100%;
        }
        .category .banner-text p {
            font-family: museo-sans, sans-serif;
            font-size: 13px;
            font-weight: 300;
            letter-spacing: 1px;
            line-height: 19.5px;
            text-align: center;
            text-size-adjust: 100%;
            text-transform: uppercase;
        }
        .container {
            max-width: 1300px;
        }
        #main-color {
            background-color: #F7F1EC;
        }
        .service-details #service-details-banner:after,
        .service .service-banner:after
        {
            content: '';
            position: absolute;
            top: 0;
            left: 0px;
            width: 100%;
            height: 100%;
            background-color: #624938bd;
        }

        .service .banner-text,
        .service-details .banner-text {
            z-index: 99;
        }

        .service .banner-text h2,
        #service-details-title {
            color: #FFF;
        }
        #service-details-content p:first-child {
            margin: 0px;
        }
        .btn.btn-primary {
            background: rgb(201, 173, 149);
            padding: 12px 24px;
            margin: 0;
            border-radius: 0px;
            font-size: 13px;
            text-transform: uppercase;
            border: 0px !important;
        }
        .btn.btn-primary:hover {
            background-color: rgb(133, 106, 87);
        }

        .btn.btn-primary:active {
            border: 0px !important;
            background-color:  rgb(201, 173, 149) !important;
        }

        .btn.btn-primary:focus {
            box-shadow: 0 0 0 .2rem rgba(201, 173, 149, 0.5) !important;
        }

        
        .btn.btn-success {
            background-color: rgb(133, 106, 87);
            padding: 12px 24px;
            margin: 0;
            border-radius: 0px;
            font-size: 13px;
            text-transform: uppercase;
            border: 0px !important;
            color: #FFF !important;
        }
        .btn.btn-success:hover {
            background: rgb(201, 173, 149);
            border: 0px !important;
        }
        .btn.btn-success:active {
            background-color: rgb(133, 106, 87) !important;
            border: 0px !important;
        }

        .btn.btn-success:focus {
            box-shadow: 0 0 0 .2rem rgba(133, 106, 87, 0.5) !important;
        }
        .card-body {
            position: relative;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            align-items: flex-start;
        }

        .clinic-buttons {
            display: flex;
            justify-content: space-between;
        }
        .clinic-buttons .btn {
            width: 48%;
        }

        #categories {
            margin: 0px !important;
        }
        .service, .service-details {
            padding: 0px 15px;
        }

    </style>
</head>
<body>
        <div id="categories" class="row">
"""

# Loop through categories to create the category view
for category in categories_data:
    image_url = image_urls.get(category['name'].upper(), '')
    html_content += f"""
        <div class="col-md-3 mb-4 category active" id="category-card-{category['id']}">
            <div class="card category-card" data-category-id="{category['id']}" style="background-image: url('{image_url}');">
            </div>
            <div class="banner-text">
                <h2>{category['name']}</h2>
                <p>Se behandlinger</p>
            </div>
        </div>
    """

# Loop through categories and services to create the service view
for category in categories_data:
    html_content += f"""
        <div class="service" id="category-{category['id']}">
            <div class="service-banner" style="background-image: url('{image_urls.get(category['name'].upper(), '')}');">
                <div class="banner-text">
                    <h2>{category['name']}</h2>
                </div>
            </div>
            <button type="button" class="btn btn-secondary mb-4 mt-3 back-to-categories">Tilbage</button>
            <div class="row">
    """
    for service in category['services']:
        service_id = service['service_id']
        description = service.get('description', '')
        button_text = "Læs mere" if description else "Bestil tid"
        button_class = "btn-primary" if description else "btn-success"
        html_content += f"""
                <div class="col-md-4 mb-4">
                    <div class="card h-100 service-card" data-service-id="{service_id}">
                        <div class="card-body">
                            <h5 class="card-title">{service['name']}</h5>
                            <p class="card-text mb-0"><strong>Duration:</strong> {service.get('duration', 'N/A')}</p>
                            <p class="card-text"><strong>Price:</strong> {service.get('price', 'N/A')}</p>
                            <button type="button" class="btn {button_class} view-service-details" data-service-id="{service_id}" data-description="{1 if description else 0}">
                                {button_text}
                            </button>
                        </div>
                    </div>
                </div>
        """
    html_content += "</div></div>"

# Add service details section
html_content += """
    <div class="service-details" id="service-details">
        <div class="service-banner" id="service-details-banner">
            <div class="banner-text">
                <h2 id="service-details-title"></h2>
            </div>
        </div>
        <button type="button" class="btn btn-secondary mt-3 mb-4 back-to-services">Tilbage</button>

        <div id="service-details-content"></div>
    </div>
"""

# End of HTML content
html_content += """
        </div>
    <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    <script>
        var categories_data = """ + json.dumps(categories_data) + """;
        var currentCategoryId = null;
        var image_urls = {
            "ANSIGTSBEHANDLINGER": "http://www.feminine.aveo19.dk/wp-content/uploads/woman-making-facial-treatment-in-a-beauty-saloon.jpg",
            "KROPSBEHANDLINGER": "http://www.feminine.aveo19.dk/wp-content/uploads/spa-massage-indian-woman-relaxing-on-table-while-therapist-massaging-her-shoulders.jpg",
            "VIPPE & BRYN BEHANDLINGER": "http://www.feminine.aveo19.dk/wp-content/uploads/IMG_1408.jpg",
            "LYCON VOKSBEHANDLINGER": "http://www.feminine.aveo19.dk/wp-content/uploads/liquid-sugar-wax-on-spatula-beige.jpg",
            "PAKKER": "http://www.feminine.aveo19.dk/wp-content/uploads/beauty-box-wellness-zero-waste-gift-natural-organic-spa-care-package-handmade-eco-box-mental.jpg"
        };

        $(document).ready(function() {
            // Show the categories initially
            $('.category').addClass('active');
            
            // Function to get URL parameters
            function getUrlParameter(name) {
                name = name.replace(/[\\[]/, '\\[').replace(/[\\]]/, '\\]');
                var regex = new RegExp('[\\?&]' + name + '=([^&#]*)');
                var results = regex.exec(window.location.search);
                return results === null ? '' : decodeURIComponent(results[1].replace(/\\+/g, ' '));
            }

            var initialCategoryId = getUrlParameter('category');
            var initialServiceId = getUrlParameter('service');

            // Show services when category card is clicked
            $('.category-card').on('click', function() {
                currentCategoryId = $(this).data('category-id');
                updateUrl({ category: currentCategoryId });
                $('.category').removeClass('active');
                $('.service').removeClass('active');
                $('#category-' + currentCategoryId).addClass('active');
            });

            // Show service details when "Læs mere" button is clicked
            $('.view-service-details').on('click', function() {
                var serviceId = $(this).data('service-id');
                var hasDescription = $(this).data('description');
                if (!hasDescription) {
                    var url = "https://feminine.planway.com/?d=28822&sid=" + serviceId;
                    window.location.href = url;
                    return;
                }
                updateUrl({ category: currentCategoryId, service: serviceId });
                showServiceDetails(serviceId);
            });

            function showServiceDetails(serviceId) {
                var service = getServiceById(serviceId);
                if (service) {
                    $('#service-details-title').text(service.name);
                    var content = '<p><strong>Varighed:</strong> ' + service.duration + '</p>';
                    content += '<p><strong>Pris:</strong> ' + service.price + '</p>';
                    if (service.description) {
                        content += '<p>' + service.description.replace(/\\n/g, '<br>') + '</p>';
                    }
                    content += '<div class="clinic-buttons">';
                    content += '<a href="https://feminine.planway.com/?d=10752&sid=' + service.service_id + '" class="btn btn-success">Bestil tid i Hjemmeklinik</a>';
                    content += '<a href="https://feminine.planway.com/?d=28822&sid=' + service.service_id + '" class="btn btn-success">Bestil tid i Klinik</a>';
                    content += '</div>';
                    $('#service-details-content').html(content);

                    var category = getCategoryByServiceId(serviceId);
                    if (category) {
                        var imageUrl = image_urls[category.name.toUpperCase()];
                        $('#service-details-banner').css('background-image', 'url(' + imageUrl + ')');
                    }

                    $('.service').removeClass('active');
                    $('.service-details').addClass('active');
                }
            }

            // Back to categories
            $('.back-to-categories').on('click', function() {
                updateUrl({});
                $('.service').removeClass('active');
                $('.category').addClass('active');
                currentCategoryId = null;
            });

            // Back to services
            $('.back-to-services').on('click', function() {
                updateUrl({ category: currentCategoryId });
                $('.service-details').removeClass('active');
                $('#category-' + currentCategoryId).addClass('active');
            });

            // Get service by ID
            function getServiceById(serviceId) {
                var service = null;
                for (var i = 0; i < categories_data.length; i++) {
                    var category = categories_data[i];
                    for (var j = 0; j < category.services.length; j++) {
                        var currentService = category.services[j];
                        if (String(currentService.service_id) === String(serviceId)) {
                            service = currentService;
                            break;
                        }
                    }
                    if (service) {
                        break;
                    }
                }
                return service;
            }

            // Get category by service ID
            function getCategoryByServiceId(serviceId) {
                var category = null;
                for (var i = 0; i < categories_data.length; i++) {
                    var currentCategory = categories_data[i];
                    for (var j = 0; j < currentCategory.services.length; j++) {
                        if (String(currentCategory.services[j].service_id) === String(serviceId)) {
                            category = currentCategory;
                            break;
                        }
                    }
                    if (category) {
                        break;
                    }
                }
                return category;
            }

            // Update the URL with new parameters
            function updateUrl(params) {
                var url = new URL(window.location.href);
                Object.keys(params).forEach(key => {
                    if (params[key]) {
                        url.searchParams.set(key, params[key]);
                    } else {
                        url.searchParams.delete(key);
                    }
                });
                history.pushState({}, '', url);
            }

            // If URL has category or service parameters, display the relevant sections
            if (initialCategoryId) {
                $('.category').removeClass('active');
                $('.service').removeClass('active');
                $('#category-' + initialCategoryId).addClass('active');
                currentCategoryId = initialCategoryId;
                if (initialServiceId) {
                    showServiceDetails(initialServiceId);
                }
            }
        });
    </script>
</body>
</html>
"""

# Write the HTML content to the file
with open(output_html_path, "w", encoding="utf-8") as html_file:
    html_file.write(html_content)

print(f"HTML file generated at {output_html_path}")
