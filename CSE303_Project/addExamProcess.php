<?php
session_start();
require_once 'core/init.php';



	
	if(isset($_POST['addExamButton'])){
			$target_dir = "uploads/";
			$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
			move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file);

				$query = "INSERT INTO exams(title, year, semester, marks, examtype, question)
						  Values ('".$_POST['title']."', '".$_POST['year']."','".$_POST['semester']."','".$_POST['marks']."','".$_POST['examType']."','$target_file')";
				$result1 = $db->query($query);

				//$_SESSION['User']=$_POST['firstname'];
				header("location:teacherIndex.php");
				echo "<script type='text/javascript'>alert('Question Uploaded');</script>";
				die();
			}
		
?>