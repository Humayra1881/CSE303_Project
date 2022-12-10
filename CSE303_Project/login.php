<form action="loginprocess.php" method="post">
    <input class="text email form-control" type="text" name="username" placeholder="Username" required="" >
    <br>
    <input class="text form-control" type="password" name="password" placeholder="Password" required="" style="margin-top: 10px;">
    <br>
    <select name="loginType" class="form-control">
        <option value="students">Student</option>
        <option value="teachers">Teachers</option>
        <option value="admin">Admin</option>
    </select>
    <br>
    <input type="submit" value="SIGN IN" name="loginbutton" class="form-control">
</form>