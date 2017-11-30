<?php
use \Psr\Http\Message\ServerRequestInterface as Request;
use \Psr\Http\Message\ResponseInterface as Response;
$app = new \Slim\App;

$app->get('/api/menu/type', function(Request $request, Response $response) {
	echo "mexican sounds nice?";
});
$app->get('/api/menu/ant', function(){
	//$db = new db();
	/*$query = "select * from menus where dish_name='ant legs'";
	$result = $mysqli->query($query);
	while($row = $result->fetch_assoc()){
		$data[] = $row;
	}
	if(isset($data)){

		header('Content-Type: application/json');

		echo json_encode($data);
	}*/
	$sql = "SELECT * FROM menus where dish_name='ant legs'";

    try{
        // Get DB Object
        $db = new db();
        // Connect
        $db = $db->connect();

        $stmt = $db->query($sql);
        $menus = $stmt->fetchAll(PDO::FETCH_OBJ);
        $db = null;
        echo json_encode($menus);
    } catch(PDOException $e){
        echo '{"error": {"text": '.$e->getMessage().'}';
    }

});

/*$app->post('/api/menu/add', function(Request $request, Response $response){
    $dish_name = $_POST('dish_name');
   // $dish_price = $request->getParam('dish_price');
   // $dish_pic = $request->getParam('dish_pic');

    echo $dish_name;

    $sql = "INSERT INTO menus (dish_name,dish_price,dish_pic) VALUES
    ('$dish_name','$dish_price','$dish_pic')";
    
    $result = $mysqli->query($sql);

    if(!mysqli_query($mysqli, $sql)){
    	echo 'error';
    }
    else{
    	echo 'inserted';
    }
    header("refresh:2; url=home.html"); */
$app->post('/api/menu/add', function(Request $request, Response $response){
    $dish_name =  $request->getParam('dish_name');
    $dish_price = $request->getParam('dish_price');
    $dish_pic = $request->getParam('dish_pic');

    $sql = "INSERT INTO menus (dish_name,dish_price,dish_pic) VALUES
    (:dish_name,:dish_price,:dish_pic)";

    try{
        // Get DB Object
        $db = new db();
        // Connect
        $db = $db->connect();

        $stmt = $db->prepare($sql);

        $stmt->bindParam(':dish_name', $dish_name);
        $stmt->bindParam(':dish_price',  $dish_price);
        $stmt->bindParam(':dish_pic',      $dish_pic);

        $stmt->execute();

        echo '{"notice": {"text": "Customer Added"}';

    } catch(PDOException $e){
        echo '{"error": {"text": '.$e->getMessage().'}';
    }
});
