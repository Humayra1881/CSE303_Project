
<?php
	session_start();
	if(!isset($_SESSION['User']))
		header("location:index.php");
	require_once 'core/init.php';
	include 'includes/header.php';
?>


<?php
	echo "<h1>Hello Student: </h1>";
?>

<button onclick="window.location.href='viewExamsStudents.php'">View Exams</button>
<button onclick="window.location.href='logout.php'">Logout</button>