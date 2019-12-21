let child = $("header nav li a:contains(Machine Learning)");
child.html(child.html() + ' <span class="sr-only">(current)</span>');
let parent = child.closest('li');
parent.attr("class", parent.attr("class") + " active");


