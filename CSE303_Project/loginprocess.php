<?php
	session_start();
	require_once 'core/init.php';
	if(isset($_POST['loginbutton'])){
		if($_POST['loginType'] == "teachers"){
			$query = "SELECT * FROM teachers WHERE username = '".$_POST['username']."' and password = '".$_POST['password']."'";
			$result = mysqli_query($db, $query);

			if(mysqli_fetch_assoc($result)){
				$_SESSION['User']=$_POST['username'];
				$_SESSION['LoginType'] = "Teachers";
				header("location:teacherIndex.php");
				echo "<script type='text/javascript'>alert('LOGIN SUCCESSFUL AS TEACHER');</script>";
				exit();
			}
			else{
				header("location: login.php");
				echo "<script type='text/javascript'>alert('Please enter correct username or password');</script>";
			}
		}else if($_POST['loginType'] == "students"){
			$query = "SELECT * FROM students WHERE username = '".$_POST['username']."' and password = '".$_POST['password']."'";
			$result = mysqli_query($db, $query);

			if(mysqli_fetch_assoc($result)){
				$_SESSION['User']=$_POST['username'];
				$_SESSION['LoginType'] = "Students";
				header("location:studentIndex.php");
				echo "<script type='text/javascript'>alert('LOGIN SUCCESSFUL AS Student');</script>";
				exit();
			}
			else{
				header("location: login.php");
				echo "<script type='text/javascript'>alert('Please enter correct username or password');</script>";
			}
		}else{
			$query = "SELECT * FROM admins WHERE username = '".$_POST['username']."' and password = '".$_POST['password']."'";
			$result = mysqli_query($db, $query);

			if(mysqli_fetch_assoc($result)){
				$_SESSION['User']=$_POST['username'];
				$_SESSION['LoginType'] = "Students";
				header("location:adminIndex.php");
				echo "<script type='text/javascript'>alert('LOGIN SUCCESSFUL AS ADMIN');</script>";
				exit();
			}
			else{
				header("location: login.php");
				echo "<script type='text/javascript'>alert('Please enter correct username or password');</script>";
			}
		}

	}
		
?>