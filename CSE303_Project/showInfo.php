<?php
	session_start();
	require_once 'core/init.php';
	if(isset($_POST['showbutton'])){
		if($_POST['showInfo'] == "teachers"){
			header("location:showTeachers.php");
			exit();
		}else if($_POST['showInfo'] == "students"){
			header("location:showStudents.php");
			exit();
		}else if($_POST['showInfo'] == "admin"){
			header("location:showAdmins.php");
			exit();
		}
	}

?>