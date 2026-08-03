def movie_festival(movies):
    movies.sort(key=lambda m: m[1])
    count, current_end = 0, 0
    for start, end in movies:
        if start >= current_end:
            count += 1
            current_end = end
    return count

n = int(input())
m = []
for i in range(n):
    new = input().split(" ")
    m.append()
print(movie_festival())