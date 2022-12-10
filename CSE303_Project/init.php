<?php
	$db = mysqli_connect('127.0.0.1','root','','spms');
	if(mysqli_connect_errno()){
		echo 'Database Connection Failed With Following Errors: '.mysqli_connect_error();
		die();
	}
?>

