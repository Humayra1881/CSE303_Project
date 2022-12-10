<form action="addExamProcess.php" method="post" enctype="multipart/form-data">
    <input class="text form-control" type="text" name="title" placeholder="Subject Name" required="">
    <select name="year" class="form-control">
        <option value="2022">2022</option>
        <option value="2021">2021</option>
    </select>
    <select name="semester" class="form-control">
        <option value="Autumn">Autumn</option>
        <option value="Spring">Spring</option>
        <option value="Summer">Summer</option>
    </select>
    <input class="text form-control" type="text" name="marks" placeholder="Marks" required="">
    <select name="examType" class="form-control">
        <option value="Quiz">Quiz</option>
        <option value="Mid">Mid</option>
        <option value="Final">Final</option>
    </select>
    <input type="file" name="fileToUpload" id="fileToUpload" class="form-control">
    
    <input type="submit" value="submit" name="addExamButton" class="form-control">
</form>