<?php
error_reporting(0);
$connection = mysql_connect("localhost", "root", "");
$db = mysql_select_db("gobana", $connection);
if(isset($_POST['delete']))
    {
        echo "<div id='overlay'><th><form action='' method='post'>
                    <center><h3>You are going to delete a user.Are you sure?</h3></center> 
                    <input type='text'  name='name' value=\"$_POST[name] \" >
                    <input type='hidden'  name='id' value=\"$_POST[id] \" >
                    <input id='confirm' name='yes' type='submit' value='confirm'>
                    <input id='abort' name='yes' type='submit' value='abort'>
                    </form></th>
                    </div>";
        
            
    }       
if(isset($_POST['yes']))
    {
        if($_POST['yes']=='confirm')
        {
            $id=$_POST['id'];   
            mysql_query("DELETE from user where id='$id'", $connection);
            mysql_query("DELETE from pdf where owner='$id'", $connection); 
            mysql_query("DELETE from comments where owner='$id'", $connection); 
            mysql_query("DELETE from book where owner='$id'", $connection);  
            
        }   
    }   
    

?>
<!DOCTYPE html>
<html>
<head>
<title>BOOKS</title>
<link href="style.css" rel="stylesheet" type="text/css">
</head>
<body>
<table width="100%">
    <tr>
<td style="width:90%" >
<table style="width:100%; margin-top:55px; border: 1px solid black; ">
    <caption><center><h1>ADMIN PANEL</h1></center></caption>
    
    <caption><center><h3>Remove a user</h3></center></caption>
    <tr style='border: 1px solid black;' >
        <th style='border: 1px solid black;' >S.no.</th>
        <th style='border: 1px solid black;' >Name</th>
        <th style='border: 1px solid black;' >Email</th>
        <th style='border: 1px solid black;' >Delete</th>
    </tr>
    <?php
    $n=0;
    $resultp=mysql_query("SELECT * FROM user order by id", $connection);
    $rowsp = mysql_num_rows($resultp);
    $i=1;
    
    while($i<=$rowsp)
    {
        echo "<tr style='border: 1px solid black;' >";
        if($rowp = mysql_fetch_array($resultp))
        { 
            echo "<th style='border: 1px solid black;' >".$i."</th>";
            echo "<th style='border: 1px solid black;' >"."$rowp[user]"."</th>";
            echo "<th style='border: 1px solid black;' >"."$rowp[email]"."</th>";
            echo "<th><form action='' method='post'>
                    <input type='hidden' name='id' value=\"$rowp[id]\" >
                    <input type='hidden' name='name' value=\"$rowp[user]\" >
                    <input id='delete' name='delete' type='submit' value='delete'>
                    </form></th>";
            
        }
        $i=$i+1;
        echo "</tr>";
    }
    
        
?>
</td>
</tr>

</table>
</table>
</div>
</body>
</html>