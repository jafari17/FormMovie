
const table = document.querySelector('table');
const tbody = document.querySelector('tbody');
const csrf = $("input[name=csrfmiddlewaretoken]").val()
const My_URL = location.href;
// let url2 = document.getElementById().value
const url_id = My_URL.substring(My_URL.lastIndexOf('/') + 1 )
console.log(url_id)


const form = document.querySelector('form');
const input_movie_name = document.querySelector('#movie_name');
const input_director = document.querySelector('#director');
const input_release_date = document.querySelector('#release_date');
const input_Genre = document.querySelector('#Genre');
const input_imdb = document.querySelector('#imdb');


document.addEventListener('DOMContentLoaded', function load(e){
    let url_get = ('/edit/get/'+ url_id)
    $.ajax({
        url: "http://127.0.0.1:8000/edit/ajax",
        type: 'GET',
        dataType: 'json',
        data:{
             movie_id: url_id
        },
        success: function(data) {
              // Handle the data returned from the server

        load(data)
        },
        error: function(xhr, status, error) {
              // Handle error situations
        console.error('Error:', status, error);
        }})


    function load (data){

        let tasks = data
        console.log(data)

            input_movie_name.value = tasks.movie_name
            input_director.value = tasks.director
            input_release_date.value = tasks.release_date
            input_Genre.value = tasks.Genre
            input_imdb.value = tasks.imdb

    }
})

// const button = document.querySelector('.button');
// button.addEventListener('click', function (){
    console.log('hi ajax post')
    data = 'post_test'
    // let url_post = ('/edit/post/'+ url_id)
    console.log(url_id)

function StartAjax(){


    let tasks = {}
    tasks.movie_name = input_movie_name.value
    tasks.director = input_director.value
    tasks.release_date = input_release_date.value
    tasks.Genre = input_Genre.value
    tasks.imdb = input_imdb.value

    console.log('start ajax')
    $.ajax({
        url: "http://127.0.0.1:8000/edit/ajax/",
        type: 'POST',
        dataType: 'json',
        data:{
            csrfmiddlewaretoken: csrf,
            movie_id: url_id,
            movie_name: tasks.movie_name,
            director : tasks.director,
            release_date : tasks.release_date,
            Genre : tasks.Genre,
            imdb : tasks.imdb,

        },
        success: function(data) {
            console.log('ajax success')
              // Handle the data returned from the server
        },
        error: function(xhr, status, error) {
              // Handle error situations
        console.error('Error:', status, error);

         }})

}


