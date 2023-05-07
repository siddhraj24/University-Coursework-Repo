<html>

<head>

  <title>Message Board</title>
  <link rel="stylesheet" href="stylesheet.css">
</head>

<body>
  <div class="format">
    <form method="get" action="board.php">
      <input id="one" type="submit" name="logout" value="logout" />
    </form>
    <form action=board.php method=POST>
      <input size=60 type="text" id="new_msg" name="new_msg" /><br><br>
      <input id=newmg type="submit" name="submit" value="New Post" />
    </form>
    <?php
  
  session_start();
error_reporting(E_ALL);
ini_set('display_errors','On');
//connecting to database
try {
  $conn = new PDO("mysql:host=127.0.0.1:3306;dbname=board","root","",array(PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION));
 //if user select logout,redirect to login page
  if(isset($_GET['logout'])){
    session_destroy();
    header('Location: login.php');
    exit();
  }
  //if user and pass are right , go to board
  if(isset($_POST['username']) && isset($_POST['password'])){
    $query = 'SELECT username,password from USERS where username="'.$_POST['username'].'"';
    $result = $conn->query($query,PDO::FETCH_ASSOC);
    $result = $result->fetchAll();
    if($result[0]['password']== md5($_POST['password'])){
      $_SESSION["message_board"] = $result[0]['username'];
    }
    else{
      header('Location: login.php');
    exit();
    }
  }
  if(isset( $_SESSION['message_board'])){
  if(isset($_POST["new_msg"])){
  $insert = 'INSERT INTO POSTS VALUES(:id,:replyto,:postedby,now(),:message)';
  $res = $conn->prepare($insert, array(PDO::ATTR_CURSOR => PDO::CURSOR_FWDONLY));
  $res->execute(array(':id' => uniqid(), ':replyto' => null, ':postedby'=> $_SESSION['message_board'],':message'=> $_POST['new_msg']));
  echo "Message Posted...!!!!";
  }
   if(isset($_GET["replyto"])){
   $uuid = uniqid();
   $insert = 'INSERT INTO POSTS VALUES(:id,:replyto,:postedby,now(),:message)';
   $res = $conn->prepare($insert, array(PDO::ATTR_CURSOR => PDO::CURSOR_FWDONLY));
   $res->execute(array(':id' => $uuid, ':replyto' => null, ':postedby'=> $_SESSION['message_board'],':message'=> $_GET['reply']));
   $update = 'UPDATE posts SET replyto=:replyid where id=:uid';
   $res = $conn->prepare($update, array(PDO::ATTR_CURSOR => PDO::CURSOR_FWDONLY));
   $res->execute(array(':replyid' =>$_GET['replyto'] , ':uid'=>$uuid));
   echo "Reply Posted...!!!!";
   }
   $conn->beginTransaction();
  $conn->exec('delete from users where username="smith" or username="siddhraj" ');
  $conn->exec('insert into users values("smith","' . md5("mypass") . '","John Smith","smith@cse.uta.edu");insert into users values("siddhraj","' . md5("siddhraj") . '","siddhraj solanki","sps7988@mavs.uta.edu")')
        or die(print_r($conn->errorInfo(), true));
  $conn->commit();
   $qry = 'select * from posts inner join users where posts.postedby = users.username order by datetime DESC';
   print "<pre>"; 
  foreach ($conn->query($qry) as $row)  {
    $ID=$row['id'];
    $RPLY=$row['replyto'];
    $USER=$row['username'];
    $FULLNAME=$row['fullname'];
    $DATETIME=$row['datetime'];
    $MSG=$row['message'];
    /*$fn='aaa';
    function aaa ()
    { 
      global $RPLY;
      if($RPLY!=null)
        return $RPLY;
    }*/
    $DISP=<<<ONE
      <form>
      <input type=hidden name=replyto value=$ID>
      MSG ID: $ID
      Replied To message with ID: $RPLY
      Username:$USER
      Full Name:$FULLNAME
      Date and Time:$DATETIME
      Message:$MSG  <br>
      <input size=60 type=text id=reply name=reply><br>
      <button id=repbut type=submit formaction=board.php>Reply</button></form>
    ONE;
    echo $DISP;  
  }
  print "</pre>";
 }
 else{
  header('Location: login.php');
    exit();
 }
 } 
catch (PDOException $e) {
  print "Error!: " . $e->getMessage() . "<br/>";
  die();
}

?>
  </div>
</body>

</html>