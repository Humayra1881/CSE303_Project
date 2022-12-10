<?php
  
  session_start();
  if(!isset($_SESSION['User']))
    header("location:index.php");
  require_once 'core/init.php';
  include 'includes/header.php';
?>

<?php
      $sql = "SELECT username 
              FROM teachers 
              ";
      $pquery = $db->query($sql);
?>

<table>
  <th>Name</th>

  
  <?php while ($parent = mysqli_fetch_assoc($pquery)) : ?>
    <tr>
      <td><?php echo $parent['username'];?></td>
    </tr>
  <?php endwhile;?>
</table>