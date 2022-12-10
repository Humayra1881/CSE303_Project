
<?php
	session_start();
	if(!isset($_SESSION['User']))
		header("location:index.php");
	require_once 'core/init.php';
	include 'includes/header.php';
?>


<?php
	echo "<h1>Hello Admin: </h1>";
?>

<form action="showInfo.php" method="post">
    <select name="showInfo" class="form-control">
        <option value="students">Students</option>
        <option value="teachers">Faculty Members</option>
        <option value="admin">Admin</option>
    </select>
    <input type="submit" value="SHOW" name="showbutton" class="form-control">
</form>
<button onclick="window.location.href='logout.php'" class="btn btn-dark">Logout</button>