//subscribe to the fav resto list

/*
 
 function fun()
 {
 $.get('\addEmail.php', {email : $(this).val()}, function(data) {
 //here you would write the "you ve been successfully subscribed" div
 });
 }
 
 */

// input would be
//<input type="button" value="subscribe" class="submit" onclick="fun();" />


mysql_connect("localhost","root","");
mysql_select_db("eciticket_db");

error_reporting(E_ALL && ~E_NOTICE);

$email=mysql_real_escape_string($_GET['email']);
$sql="INSERT INTO newsletter_email(email) VALUES ('$email')";
$result=mysql_query($sql);
if($result){
    echo "You have been successfully subscribed.";
}
if(!$sql)
die(mysql_error());

mysql_close();