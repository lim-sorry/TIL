<template>
  <div>
    <!-- 장르 dropdown-->
    <div class="form-row mb-2 d-flex align-items-center">
      <div class="col-auto my-1">
        <select
          class="custom-select mr-sm-2"
          v-model="selectedGenre"
          id="genreSelect"
        >
          <option disabled value="">장르</option>
          <option>전체</option>
          <option>액션</option>
          <option>모험</option>
          <option>애니메이션</option>
          <option>코미디</option>
          <option>범죄</option>
          <option>드라마</option>
          <option>가족</option>
          <option>판타지</option>
          <option>역사</option>
          <option>공포</option>
          <option>음악</option>
          <option>미스터리</option>
          <option>로맨스</option>
          <option>SF</option>
          <option>TV 영화</option>
          <option>스릴러</option>
          <option>전쟁</option>
          <option>서부</option>
        </select>
      </div>
        <h4 class="text-light mb-0 mx-2">영화를 선택해보세요</h4>
    </div>

    <!--영화목록-->
    <div class="row row-cols-3 row-cols-md-5">
      <MovieCard
        v-for="(movie, idx) in selectedMovies"
        :key="idx"
        :movie="movie"
      />
    </div>

    <!--ReviewFormModal-->
    <div
      class="modal fade"
      id="reviewFormModal"
      tabindex="-1"
      v-if="clickedMovie"
    >
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header d-flex justify-content-center">
            <h1 class="mb-0">
              <strong>{{ clickedMovie.title }}</strong>
            </h1>
          </div>
          <div class="modal-body">
            <!--ReviewForm-->
            <form @submit.prevent="createReview">
              <div class="form-group my-0">
                <label for="review"
                  >{{ username }}님의 후기를 들려주세요😊</label
                >
                <textarea
                  class="form-control"
                  id="review"
                  rows="5"
                  v-model="article.content"
                  placeholder="리뷰를 작성해주세요"
                ></textarea>
                <div class="d-flex justify-content-center my-2">
                  <star-rating
                    v-model="article.rating"
                    active-color="purple"
                    class="mb-2"
                  ></star-rating>
                </div>
                <div class="alert alert-info mx-5" role="alert" v-if="is_created">후기가 작성되었습니다.</div>
                <button type="submit" class="btn btn-info my-3 text-white">
                  리뷰작성
                </button>
                <button class="btn btn-danger m-3" data-dismiss="modal" @click="is_created = false">
                  닫기
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>

    <!--ReviewsModal-->
    <div class="modal fade" id="reviewsModal" tabindex="-1" v-if="clickedMovie">
      <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
        <div class="modal-content">
          <div class="modal-header d-flex justify-content-center">
            <h1 class="mb-0">
              <strong>'{{ clickedMovie.title }}' REVIEW</strong>
            </h1>
          </div>
          <div class="modal-body" v-if="movieReviews.length">
            <li v-for="(review, idx) in movieReviews" :key="idx" id="review">
              <h5>{{ review.user }}</h5>
              <p>{{ review.content }}</p>
              <p class="mt-2 d-flex align-items-center">
                👍 {{ review.like_users.length }}
                <button
                  type="button"
                  class="btn btn-outline-info btn-sm mx-2"
                  @click="clickedReview(review)"
                  data-dismiss="modal"
                >
                리뷰 보기
                </button>
              </p>

              <hr />
            </li>
            <button class="btn btn-secondary m-3" data-dismiss="modal">
              닫기
            </button>
          </div>
          <div v-else>
            <h4 class="text-center mt-4">아직 리뷰가 없군요😂</h4>
            <button class="btn btn-secondary m-3" data-dismiss="modal">
              닫기
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios"
import MovieCard from "@/components/Community/MovieCard"
import StarRating from "vue-star-rating"
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: "MovieList",
  components: {
    MovieCard,
    StarRating,
  },
  data: function () {
    return {
      selectedGenre: "",
      selectedMovies: [],
      article: {
        movie_pk: 0,
        content: "",
        rating: 0,
      },
      show: false,
      is_created: false,
    };
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem("jwt")

      const config = {
        headers: {
          Authorization: `JWT ${token}`,
        },
      };
      return config;
    },
    createReview: function () {
      const config = this.setToken();
      this.article.movie_pk = this.clickedMovie.id
      this.is_created = false

      axios.post(`${SERVER_URL}/articles/`, this.article, config)
        .then(() => {
          this.article.content = ""
          this.article.rating = 0
          this.is_created = true
          this.$store.dispatch("getReviews")
        })
        .catch((err) => {
          console.log(err);
        });
    },
    clickedReview: function (review) {
      this.$store.dispatch("clickedReview", review)
      this.$router.push({ name: 'ReviewPage'})
    },
  },
  computed: {
    movies: function () {
      return this.$store.state.movies
    },
    clickedMovie: function () {
      return this.$store.state.clickedMovie
    },
    movieReviews: function () {
      return this.$store.state.movieReviews
    },
    username: function () {
      return this.$store.state.username
    },
  },
  watch: {
    selectedGenre: function () {
      if (this.selectedGenre === "전체") {
        this.selectedMovies = this.movies
      } else {
        this.selectedMovies = this.movies.filter((movie) =>
          movie.genres.includes(this.selectedGenre)
        )
      }
    },
  },
  created: function () {
    if (this.$route.params.genre) {
      this.selectedGenre = this.$route.params.genre
      this.selectedMovies = this.movies.filter((movie) =>
        movie.genres.includes(this.selectedGenre)
      )
    } else {
      this.selectedMovies = this.$store.state.movies
    }
  },
};
</script>

<style>
#review {
  list-style: none;
  text-align: left;
}
p {
  margin: 0;
}
</style>