let names = new Map([
    ['mnist', 'Handwritten Digit'],
    ['cifar10', 'Cifar 10'],
    ['fruits', 'Fruits & Vegetables'],
    ['yolo', 'YOLO'],
    ['fcn', 'FCN'],
    ['mrcnn', 'Mask R-CNN']
]);
let project = $("#project-name").attr("value");
let sidebar_item = $("#ml-content .sidebar-sticky li a:contains('" + names.get(project) + "')");
sidebar_item.html(sidebar_item.html() + ' <span class="sr-only">(current)</span>');
sidebar_item.attr("class", sidebar_item.attr("class") + " active");
