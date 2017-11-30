<?php
use \Psr\Http\Message\ServerRequestInterface as Request;
use \Psr\Http\Message\ResponseInterface as Response;

require '../vendor/autoload.php';

$app = new \Slim\App;
require '../src/config/db.php';
//require '../src/routes/done.php';

require '../src/routes/menu.php';
require '../src/routes/customers.php';

$app->get('/hello/{name}', function (Request $request, Response $response) {
    $name = $request->getAttribute('name');
    $response->getBody()->write("Hello, $name");

    return $response;
});
/*$app->get('/api/customers', function(Request $request, Response $response){
    $sql = "SELECT * FROM customers";

    try{
        // Get DB Object
        $db = new db();
        // Connect
        $db = $db->connect();

        $stmt = $db->query($sql);
        $customers = $stmt->fetchAll(PDO::FETCH_OBJ);
        $db = null;
        echo json_encode($customers);
    } catch(PDOException $e){
        echo '{"error": {"text": '.$e->getMessage().'}';
    } */
//});
$app->run();
// 

/*<?php
use \Psr\Http\Message\ServerRequestInterface as Request;
use \Psr\Http\Message\ResponseInterface as Response;

require '../vendor/autoload.php';
///require '../src/config/db.php'; 

$app = new \Slim\App;
$app->get('/hello/{name}', function (Request $request, Response $response) {
    $name = $request->getAttribute('name');
    $response->getBody()->write("<html>
<header><title>This is title</title></header>
<body>
<h1>Hello $name </h1> <p> what is good cuh? </p>
</body>
</html>");

    return $response;
}); 

// Customer Routes
//require '../src/routes/customers.php'; 
//require '../src/routes/menu.php';
echo 'hi';


$app->run(); */

