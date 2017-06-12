<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <tittle> Uživatelská stránka </tittle>
    </head>
    <body>
        <h1>Ahoj {{name}}!</h1>
        <p>
            neexistuje
        </p>        
        <img src="{{ url_for ("static", filename = 'supercat.png')}}" alt="" height="100" width="100">
    </body>
</html>
