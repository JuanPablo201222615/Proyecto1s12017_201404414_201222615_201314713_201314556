<%-- 
    Document   : registro
    Created on : 25/03/2017, 11:31:50 PM
    Author     : dell
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Crear usuario</title>
         <link href="bootstrap.css" type="text/css" rel="stylesheet">
          <style type="text/css">
   body { background: #e6ff99 !important; }
     h1 { background: #ff8566 !important; }/* Adding !important forces the browser to overwrite the default style applied by Bootstrap */
</style>
    </head>
   <body><br><br><br>
    <center><h1>Crear usuario</h1></center>
    <br>
        <form action="Controller" method="POST" >
            <table align="center"> 
                <tr>
                    <th align ="right"> Nombre de usuario: </th>
                    <td><input type="text" name="txtusername2"></td>
                    
                </tr>
                <tr>
                    <th algin="right">Password:</th>
                    <td><input type="password" name="txtpassword2"></td>
                </tr>
                  <tr>
                    <th algin="right">Nombre completo:</th>
                    <td><input type="text" name="txtname2"></td>
                </tr>
                 <tr>
                    <th algin="right">Empresa para la que trabaja:</th>
                    <td><input type="text" name="txtempresa2"></td>
                </tr>
                 <tr>
                    <th algin="right">Departamento en el que trabaja:</th>
                    <td><input type="text" name="txtdepartamento2"></td>
                </tr>
                 <tr>
                    <td><br></td>
                </tr>
                <tr>
                    <td colspan="2" align="center"><input type="submit" name="btncreateuser" value="Crear usario" class="btn btn-primary"></td>
                </tr>
                 <tr>
                    <td><br></td>
                </tr>
                  <tr>
                    
                    <td colspan="2" align="center"><input type="submit" name="btnreturn" value="Retornar" class="btn btn-primary"></td>
                </tr>
                </table>
        </form>
    </body>
</html>
