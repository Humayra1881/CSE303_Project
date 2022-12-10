<?php
      $sql = "SELECT * 
              FROM exams 
              ";
      $pquery = $db->query($sql);
?>

<table class="table table-striped">
  <th>Subject</th>
  <th>Year</th>
  <th>Semester</th>
  <th>Marks</th>
  <th>Exam Type</th>
  <th>Question</th>

  
  <?php while ($parent = mysqli_fetch_assoc($pquery)) : ?>
    <tr>
      <td><?php echo $parent['title'];?></td>
      <td><?php echo $parent['year'];?></td>
      <td><?php echo $parent['semester'];?></td>
      <td><?php echo $parent['marks'];?></td>
      <td><?php echo $parent['examtype'];?></td>
      <td><a href="<?php echo $parent['question'];?>">Download Question</a></td>
    </tr>
  <?php endwhile;?>
</table>

<button onclick="window.location.href='logout.php'" class="btn btn-dark">Logout</button>