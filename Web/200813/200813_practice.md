# 200813 practice

## Responsive Web

![image-20200813145541293](C:\Users\JS\Desktop\seoul4\online-lecture\200813\200813_practice.assets\image-20200813145541293.png)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
  <link rel="stylesheet" href="shop.css">
  <title>Title</title>
</head>
<body>
  <!-- nav -->
  <nav class="fixed-top d-flex justify-content-between p-3 bg-light">
    <h4 class="mb-0 text-dark text-decoration-none" href="#">SAMSUNG</h4>
    <div class="d-flex">
      <a class="mx-3 mb-0 text-dark font-weight-bold text-decoration-none" href="#">Contact</a>
      <a class="mx-3 mb-0 text-dark font-weight-bold text-decoration-none" href="#">Cart</a>
      <a class="mx-3 mb-0 text-dark font-weight-bold text-decoration-none" href="#">Login</a>
    </div>
  </nav>

  <div class="container pt-5">
    <!-- section -->
    <section>
      <img class="w-100" src="images/main.png" alt="main_img">
    </section>

    <!-- article -->
    <article class="d-flex flex-column align-items-center">
      <h3 class="my-5 font-weight-bold">Our New Products</h3>
      <div class="container d-flex justify-content-center">
        <div class="row row-cols-lg-4 row-cols-md-2 row-cols-1 justify-content-center">
          <div class="col">
            <a class="text-decoration-none mx-1 my-3" href="#">
              <div class="card d-flex flex-column justify-content-center w-100">
                <img src="images/buds.jpg" class="card-img-top mb-n2" alt="...">
                <div class="card-body">
                  <h5 class="card-title mb-0 text-center text-dark">Buds</h5>
                  <h6 class="card-text text-center text-dark">179,000</h6>
                </div>
              </div>
            </a>
          </div>
          <div class="col">
            <a class="text-decoration-none mx-1 my-3" href="#">
              <div class="card d-flex flex-column justify-content-center w-100">
                <img src="images/buds.jpg" class="card-img-top mb-n2" alt="...">
                <div class="card-body">
                  <h5 class="card-title mb-0 text-center text-dark">Buds</h5>
                  <h6 class="card-text text-center text-dark">179,000</h6>
                </div>
              </div>
            </a>
          </div>
          <div class="col">
            <a class="text-decoration-none mx-1 my-3" href="#">
              <div class="card d-flex flex-column justify-content-center w-100">
                <img src="images/buds.jpg" class="card-img-top mb-n2" alt="...">
                <div class="card-body">
                  <h5 class="card-title mb-0 text-center text-dark">Buds</h5>
                  <h6 class="card-text text-center text-dark">179,000</h6>
                </div>
              </div>
            </a>
          </div>
          <div class="col">
            <a class="text-decoration-none mx-1 my-3" href="#">
              <div class="card d-flex flex-column justify-content-center w-100">
                <img src="images/buds.jpg" class="card-img-top mb-n2" alt="...">
                <div class="card-body">
                  <h5 class="card-title mb-0 text-center text-dark">Buds</h5>
                  <h6 class="card-text text-center text-dark">179,000</h6>
                </div>
              </div>
            </a>
          </div>
          <div class="col">
            <a class="text-decoration-none mx-1 my-3" href="#">
              <div class="card d-flex flex-column justify-content-center w-100">
                <img src="images/buds.jpg" class="card-img-top mb-n2" alt="...">
                <div class="card-body">
                  <h5 class="card-title mb-0 text-center text-dark">Buds</h5>
                  <h6 class="card-text text-center text-dark">179,000</h6>
                </div>
              </div>
            </a>
          </div>
          <div class="col">
            <a class="text-decoration-none mx-1 my-3" href="#">
              <div class="card d-flex flex-column justify-content-center w-100">
                <img src="images/buds.jpg" class="card-img-top mb-n2" alt="...">
                <div class="card-body">
                  <h5 class="card-title mb-0 text-center text-dark">Buds</h5>
                  <h6 class="card-text text-center text-dark">179,000</h6>
                </div>
              </div>
            </a>
          </div>
          <div class="col">
            <a class="text-decoration-none mx-1 my-3" href="#">
              <div class="card d-flex flex-column justify-content-center w-100">
                <img src="images/buds.jpg" class="card-img-top mb-n2" alt="...">
                <div class="card-body">
                  <h5 class="card-title mb-0 text-center text-dark">Buds</h5>
                  <h6 class="card-text text-center text-dark">179,000</h6>
                </div>
              </div>
            </a>
          </div>
          <div class="col">
            <a class="text-decoration-none mx-1 my-3" href="#">
              <div class="card d-flex flex-column justify-content-center w-100">
                <img src="images/buds.jpg" class="card-img-top mb-n2" alt="...">
                <div class="card-body">
                  <h5 class="card-title mb-0 text-center text-dark">Buds</h5>
                  <h6 class="card-text text-center text-dark">179,000</h6>
                </div>
              </div>
            </a>
          </div>
        </div>
      </div>
    </article>

    <!-- footer -->
    <footer class="d-flex justify-content-center mt-3 mb-5">
      <a href="https://instagram.com"><img class="mx-1" src="images/instagram.png" href="#" alt="instagram" style="width: 2rem;"></a>
      <a href="https://facebook.com"><img class="mx-1" src="images/facebook.png" href="#" alt="facebook" style="width: 2rem;"></a>
      <a href="https://twitter.com"><img class="mx-1" src="images/twitter.png" href="#" alt="twitter" style="width: 2rem;"></a>
    </footer>
  </div>
  
  <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/5opper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
</body>
</html>
```

