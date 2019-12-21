/*
* @Author: Lucien Zhang
* @Date:   2019-09-21 12:49:40
* @Last Modified by:   Lucien Zhang
* @Last Modified time: 2019-09-21 17:17:58
*/
let child = $("header nav li a:contains(Home)");
child.html(child.html() + ' <span class="sr-only">(current)</span>');
let parent = child.closest('li');
parent.attr("class", parent.attr("class") + " active");
