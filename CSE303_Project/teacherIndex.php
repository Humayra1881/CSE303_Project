
<?php
	session_start();
	if(!isset($_SESSION['User']))
		header("location:index.php");
	require_once 'core/init.php';
	include 'includes/header.php';
?>


<?php
	echo "<h1>Hello Teacher: </h1>";
?>

<button onclick="window.location.href='addExam.php'" class="btn btn-dark">Add Exam</button>
<button onclick="window.location.href='viewExams.php'" class="btn btn-dark">View Exams</button>
<button onclick="window.location.href='logout.php'" class="btn btn-dark">Logout</button>