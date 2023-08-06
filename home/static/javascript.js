//
// const table = document.querySelector('table');
// const tbody = document.querySelector('tbody');
//
//
//
// document.addEventListener('DOMContentLoaded', function load(e){
//
//     $.ajax({
//         url: '/registermovie/data/',
//         type: 'GET',
//         dataType: 'json',
//         success: function(data) {
//               // Handle the data returned from the server
//         load(data)
//         },
//         error: function(xhr, status, error) {
//               // Handle error situations
//         console.error('Error:', status, error);
//         }})
//
//
//     function load (data){
//
//         let tasks = data
//         console.log(data)
//
//         const th = `<tr ><td class="name">نام</td><td class="name">کارگردان</td> <td class="name">سال ساخت</td><td class="name">ژانر</td><td class="name">نمره imdb</td></tr>`;
//
//         table.innerHTML += th;
//         for(let item of tasks){
//
//             const spanName = document.createElement('td');
//             spanName.className = 'name';
//             spanName.textContent = item.movie_name;
//
//             const spanDirector = document.createElement('td');
//             spanDirector.className = 'name';
//             spanDirector.textContent = item.director;
//
//             const spanRelease_date = document.createElement('td');
//             spanRelease_date.className = 'name';
//             spanRelease_date.textContent = item.release_date;
//
//             const spanGenre = document.createElement('td');
//             spanGenre.className = 'name';
//             spanGenre.textContent = item.Genre;
//
//             const spanImdb = document.createElement('td');
//             spanImdb.className = 'name';
//             spanImdb.textContent = item.imdb;
//
//             const link = "/delete/" + item.id
//             const spanDelete = `<td><span  class="delete"><a href=` + link+   `>  حذف </a></span></td>`;
//
//             const tr = document.createElement('tr');
//
//             tr.appendChild(spanName);
//             tr.appendChild(spanDirector);
//             tr.appendChild(spanRelease_date);
//             tr.appendChild(spanGenre);
//             tr.appendChild(spanImdb);
//
//             tr.innerHTML += spanDelete;
//             table.appendChild(tr);
//         }
//
//     }
// })
