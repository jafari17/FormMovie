list_data =[{'id': 1, 'movie_name': 'Matrix', 'director': 'lana', 'release_date': '1999', 'Genre': 'sf', 'imdb': '8.9'}, {'id': 2, 'movie_name': 'Django', 'director': 'Tarantino', 'release_date':
 '2012', 'Genre': 'action', 'imdb': '8.5'}, {'id': 3, 'movie_name': 'شب های برره ', 'director': 'مدیری', 'release_date': '2005', 'Genre': 'کمدی', 'imdb': '7'}]

movie_id = 2

for item in list_data:
    print(item)
    if movie_id == item['id']:
        data = item