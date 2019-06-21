const app = new Vue({
    delimiters: ['${', '}'],
    el: '#app',
    data: {
        API_URL: 'https://insta-hoik92.c9users.io/api/',
        logo: '<i class="fas fa-headphones"></i>',
        movies: [],
        nowMovies: [],
        isDetailPage: false,
        currentMovie: {},
        review: {
            content: '',
            score: 1
        },
        movieReviews: {},
        genres: [],
        currentGenre: '',
        cookie: '',
        isReviewUser: false,
        loginUser: {},
    },
    computed: {
        averageScore: function () {
            const scores = this.movieReviews.map(review => review.score)
            let sum = 0
            scores.forEach(score => {
                sum += score
            })
            if (sum === 0){
                return (0).toFixed(2)
            }
            return (sum / scores.length).toFixed(2)
        },
    },
    methods: {
        togglePage: function () {
            this.isDetailPage = !this.isDetailPage
        },
        getMovies: function () {
            this.isDetailPage = false
            return axios.get(this.API_URL + 'movies/')
                .then(response => {
                    this.movies = response.data
                    this.nowMovies = response.data
                    this.movies.forEach(movie => {
                        this.getAvgScore(movie)
                    })
                    return this.nowMovies
                })
        },
        setCurrentMovie: function (movie) {
            this.getMovieReviews(movie.id)
                .then(response => {
                    this.togglePage()
                })
            this.currentMovie = movie
        },
        postReview: function (movieId) {
            axios.post(`${this.API_URL}movies/${movieId}/scores/`,
               this.review,
               {
                   headers: {
                       'X-CSRFTOKEN': this.cookie,
                   }
               }
            ).then(response => {
                    alert(response.data.message)
                    this.review.content = ''
                    this.review.score = 1
                    this.getMovieReviews(movieId)
            })
            .catch(error => {
                console.log(error)
            })
        },
        getMovieReviews: function (movieId) {
            return axios.get(`${this.API_URL}movies/${movieId}/scores/`)
                .then(response => {
                    this.movieReviews = response.data
                })
        },
        getGenres: function () {
            axios.get(`${this.API_URL}genres/`)
                .then(response => {
                    this.genres = response.data
                })
        },
        setGenre: function (genreId) {
            // this.getMovies()
            //     .then(movies => {
            //         // console.log(this.movies)
            //         this.movies = []
            //         movies.filter(movie => {
            //             // return movie.genres.id === genreId
            //             for (genre of movie.genres) {
            //                 if (genre.id === genreId) {
            //                     this.movies.push(movie)
            //                 }
            //             }
            //         })
            //     })
            this.nowMovies = []
            this.movies.filter(movie => {
                for (genre of movie.genres) {
                    if (genre.id === genreId) {
                        this.nowMovies.push(movie)
                    }
                }
            })
        },
        getAvgScore: function (movie) {
            let sum = 0
            movie.scores.forEach(score => {
                sum += score.score
            })
            if (movie.scores.length === 0) {
                movie.score = (0).toFixed(2)
            } else {
                movie.score = (sum / movie.scores.length).toFixed(2)
            }
        },
        getCookie: function(name) {
           var cookieValue = null;
           if (document.cookie && document.cookie !== '') {
               var cookies = document.cookie.split(';');
               for (var i = 0; i < cookies.length; i++) {
                   var cookie = cookies[i].trim();
                   // Does this cookie string begin with the name we want?
                   if (cookie.substring(0, name.length + 1) === (name + '=')) {
                       cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                       break;
                   }
               }
           }
           return cookieValue;
        },
        getUser: function() {
            axios.get(`${this.API_URL}accounts/login_user/`)
            .then(response => {
                this.loginUser = response.data
            })
        },
        deleteReview: function (scoreId) {
            axios.delete(`${this.API_URL}scores/${scoreId}/`,
            {
                headers: {
                    'X-CSRFTOKEN': this.cookie,
                }
            }
            ).then(response => {
                    alert(response.data.message)
                    this.getMovieReviews(this.currentMovie.id)
            })
        },
    },
    created: function () {
        this.getMovies()
        this.getGenres()
        this.cookie = this.getCookie('csrftoken')
    },
    watch: {
        isDetailPage: function () {
            if (this.isDetailPage === true) {
                this.getUser()
            }
        }
    }
})