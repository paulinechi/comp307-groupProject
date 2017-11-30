<?php
use \Psr\Http\Message\ServerRequestInterface as Request;
use \Psr\Http\Message\ResponseInterface as Response;

session_start();

$app = new \Slim\App;
require 'menu.php';
/*$app->options('/{routes:.+}', function ($request, $response, $args) {
    return $response;
});

$app->add(function ($req, $res, $next) {
    $response = $next($req, $res);
    return $response
            ->withHeader('Access-Control-Allow-Origin', '*')
            ->withHeader('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type, Accept, Origin, Authorization')
            ->withHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS');
});*/

// Get All Customers
$app->get('/api/customers', function(Request $request, Response $response){
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
    }
});

// Get Single Customer
$app->get('/api/customer/{id}', function(Request $request, Response $response){
    $id = $request->getAttribute('id');

    $sql = "SELECT * FROM customers WHERE id = $id";

    try{
        // Get DB Object
        $db = new db();
        // Connect
        $db = $db->connect();

        $stmt = $db->query($sql);
        $customer = $stmt->fetch(PDO::FETCH_OBJ);
        $db = null;
        echo json_encode($customer);
    } catch(PDOException $e){
        echo '{"error": {"text": '.$e->getMessage().'}';
    }
});

// Add Customer
$app->post('/api/signup', function(Request $request, Response $response){
    $username = $request->getParam('username');
    //$password = $request->getParam('password');
   // $type = $request->getParam('type');
   // $email = $request->getParam('email');
    //$address = $request->getParam('address');
    //$city = $request->getParam('city');
   // $state = $request->getParam('state');

     try{
        // Get DB Object
        $db = new db();
        // Connect
        $db = $db->connect();

        $stmt = $db->query("SELECT * FROM customers WHERE username='$username'"); //make sure the username is unique
        $customer = $stmt->fetch(PDO::FETCH_COLUMN);
        $db = null;
    

        
    } catch(PDOException $e){
        echo '{"error": {"text": '.$e->getMessage().'}';
    }


    // We know user email exists if the rows returned are more than 0
        if ( $customer->num_rows > 0 ) {
    
            $_SESSION['message'] = 'User with this email already exists!';
       
            return $response->withRedirect('../views/error.php', 301); //assuming such  html files exists
        }
        else{

            echo $username;

            //return $response->withRedirect('done.php', 301);
           }


   /* $sql = "INSERT INTO customers (username,password,type,email,address,city,state) VALUES
    (:username,:password,:type,:email,:address,:city,:state)";

    try{
        // Get DB Object
        $db = new db();
        // Connect
        $db = $db->connect();

        $stmt = $db->prepare($sql);

        $stmt->bindParam(':username', $username);
        $stmt->bindParam(':password',  $password);
        $stmt->bindParam(':type',      $type);
        $stmt->bindParam(':email',      $email);
        $stmt->bindParam(':address',    $address);
       // $stmt->bindParam(':city',       $city);
        //$stmt->bindParam(':state',      $state);

        $stmt->execute();

        echo '{"notice": {"text": "Customer Added"}';

    } catch(PDOException $e){
        echo '{"error": {"text": '.$e->getMessage().'}';
*/});

// Update Customer
$app->put('/api/customer/update/{id}', function(Request $request, Response $response){
    $id = $request->getAttribute('id');
    $username = $request->getParam('username');
    $password = $request->getParam('password');
    $type = $request->getParam('type');
    $email = $request->getParam('email');
    $address = $request->getParam('address');
   // $city = $request->getParam('city');
   // $state = $request->getParam('state');

    $sql = "UPDATE customers SET
				username 	= :username,
				password 	= :password,
                type		= :type,
                email		= :email,
                address 	= :address
			WHERE id = $id";

    try{
        // Get DB Object
        $db = new db();
        // Connect
        $db = $db->connect();

        $stmt = $db->prepare($sql);

        $stmt->bindParam(':username', $username);
        $stmt->bindParam(':password',  $password);
        $stmt->bindParam(':type',      $type);
        $stmt->bindParam(':email',      $email);
        $stmt->bindParam(':address',    $address);

        $stmt->execute();

        echo '{"notice": {"text": "Customer Updated"}';

    } catch(PDOException $e){
        echo '{"error": {"text": '.$e->getMessage().'}';
    }
});

// Delete Customer
$app->delete('/api/customer/delete/{id}', function(Request $request, Response $response){
    $id = $request->getAttribute('id');

    $sql = "DELETE FROM customers WHERE id = $id";

    try{
        // Get DB Object
        $db = new db();
        // Connect
        $db = $db->connect();

        $stmt = $db->prepare($sql);
        $stmt->execute();
        $db = null;
        echo '{"notice": {"text": "Customer Deleted"}';
    } catch(PDOException $e){
        echo '{"error": {"text": '.$e->getMessage().'}';
    }
});