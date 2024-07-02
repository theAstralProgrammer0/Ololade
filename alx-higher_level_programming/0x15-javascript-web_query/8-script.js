#!/usr/bin/node
$(document).ready(function() {
  $.ajax({
    url: "https://swapi-api.alx-tools.com/api/films/?format=json",
    method: "GET",
    success: function(data) {
      data.results.forEach(function(film) {
        $("#list_movies").append("<li>" + film.title + "</li>");
      });
    },
    error: function(error) {
      console.log("Error:", error);
    }
  });
});
