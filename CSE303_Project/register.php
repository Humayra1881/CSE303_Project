<form action="registerprocess.php" method="post">
    <input class="text form-control" type="text" name="username" placeholder="User Name" required="">
    <input class="text form-control" type="password" name="password" placeholder="Password" required="">
    <input class="text w3lpass form-control" type="password" name="cpassword" placeholder="Confirm Password" required="">
    <select name="registerType" class="form-control">
        <option value="students">Student</option>
        <option value="teachers">Teacher</option>
    </select>
    <input type="submit" value="SIGN UP" name="signupbutton" class="form-control">
</form>