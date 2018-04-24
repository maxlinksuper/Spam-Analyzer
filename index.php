<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <link href="https://fonts.googleapis.com/css?family=Lato:100,300,400,700,900" rel="stylesheet">
        <link rel="stylesheet" href="css/style.css">
        <script defer src="https://use.fontawesome.com/releases/v5.0.6/js/all.js"></script>
        <script type="text/javascript" src="https://code.jquery.com/jquery-2.1.4.js"></script>
        <link rel="shortcut icon" type="image/png" href="img/logo-5.png">

        <title>Spam Analyzer</title>
    </head>
    <body>

        <div class="navigation">
            <input type="checkbox" class="navigation__checkbox" id="navi-toggle">
            <label for="navi-toggle" class="navigation__button">
                <span class="navigation__icon"></span>
            </label>
            <div class="navigation__background">&nbsp;</div>
            <nav class="navigation__nav">
                <ul class="navigation__list">
                    <li class="navigation__item"><a href="#homepage" class="navigation__link">Home</a></li>
                    <li class="navigation__item"><a href="#section-app" class="navigation__link">Spam Analyzer</a></li>
                </ul>
            </nav>
        </div>

        <header class="header" id="homepage">
            <div class="header__logo-box">
                <img src="img/logo-white.png" alt="Logo" class="header__logo">
            </div>
            <div class="header__text-box">
                <h1 class="heading-primary">
                    <span class="heading-primary--main">Don't Spam Me</span>
                    <span class="heading-primary--subs">Web Application That Analyze Spam</span>
                </h1>
                <a href="#section-app" class="btn btn--white btn--animated">Search Who Spam You</a>
            </div>
        </header>

        <main>
            <section class="section-app">
                <div class="u-center-text u-margin-bottom-big u-center-top-large">
                    <h2 class="heading-secondary" id="section-app">
                        Spam Analyzer
                    </h2>
                </div>

                <div class="row">
                    <div class="col-1-of-3">
                        <h3 class="heading-tertiary u-margin-bottom-small ">
                            Input Keywords : 
                        </h3>
                        <form name="form" action="" method="get">
                            <input type="text" name="inputcolumn" id="inputcolumn" value="">
                        </form>
                        <a href="#algorithm" class="btn btn--whitegreen btn--animated">Submit</a>
                        <h3 class="heading-tertiary u-margin-bottom-small u-margin-top-medium">
                            Choose Algorithm : 
                        </h3>
                        <div id="algorithm">
                            <a href="#section-about" class="btn btn--green btn--animated" id="kmp">KMP</a>
                            <a href="#section-about" class="btn btn--green btn--animated" id="bm">Boyer-Moore</a>
                            <a href="#section-about" class="btn btn--green btn--animated" id="regex">Regular Expression</a>
                        </div>
                    </div>

                    <div class="col-2-of-3" id="posts">
                        <h3 class="heading-tertiary u-margin-bottom-small ">
                            Generated Post From Twitter API :
                        </h3>
                        <?php
                            $result = exec ("python scraper.py E:\Installer\xampp\htdocs");
                            $result_array = json_decode($result);
                            $a = 0;
                            echo '<script>';
                            echo 'var result = '. $result .';';
                            echo '</script>';
                            foreach ($result_array as $row) {
                                if ($a == 25) {
                                    break;
                                } else {
                                    $a = $a + 1;
                                    echo "<div class = \"default-box\"<p>
                                    ". $row . "
                                    </p></div>";
                                }
                            }
                        ?>         
                    </div>
                </div>
            </section>

     <script type="text/javascript" src="animations.js"></script>
    </body>
</html>
