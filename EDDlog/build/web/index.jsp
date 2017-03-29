<%-- 
    Document   : index
    Created on : 25/03/2017, 01:37:33 PM
    Author     : dell
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Login Form</title>
        <style type="text/css">
   body { background: #e6ff99 !important; }
     h1 { background: #ff8566 !important; }/* Adding !important forces the browser to overwrite the default style applied by Bootstrap */
</style>
        <link href="bootstrap.css" type="text/css" rel="stylesheet">
    </head>
   <body><br><br><br>
    <center><h1>Login</h1></center>
    <br>
        <form action="Controller" method="POST" >
            <table align="center"> 
                <tr>
                    <th align ="right"> UserName:</th>
                    <td><input type="text" name="txtusername" placeholder="Username"></td>
                    
                </tr>
                <tr>
                    <th algin="right">Password:</th>
                    <td><input type="password" name="txtpassword" placeholder="Password"></td>
                </tr>
                 <tr>
                    <th algin="right">Empresa</th>
                    <td><input type="text" name="txtempresa" placeholder="Empresa"></td>
                </tr>
                 <tr>
                    <th algin="right">Departamento</th>
                    <td><input type="text" name="txtdepartamento" placeholder="Departamento"></td>
                </tr>
                 <tr>
                    <td><br></td>
                </tr>
                <tr>
                    <td colspan="2" align="right"><input type="submit" name="btnlogin" value="LogIn" class="btn btn-primary"></td>
                </tr>
                 <tr>
                    <td><br></td>
                </tr>
                  <tr>
                    
                    <td colspan="2" align="right"><input type="submit" name="btnregister" value="Registrar Usuario" class="btn btn-primary"></td>
                </tr>
                </table>
        </form>
    </body>
</html>
