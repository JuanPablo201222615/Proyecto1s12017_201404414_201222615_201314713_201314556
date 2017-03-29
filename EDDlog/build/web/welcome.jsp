<%-- 
    Document   : welcome
    Created on : 25/03/2017, 05:37:07 PM
    Author     : dell
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>welcome</title>
          <link href="bootstrap.css" type="text/css" rel="stylesheet">
           <style type="text/css">
   body { background: #e6ff99 !important; }
     h1 { background: #ff8566 !important; }/* Adding !important forces the browser to overwrite the default style applied by Bootstrap */
</style>
    </head>
    <body bgcolor="#E6E6FA">
     <form action="Controller" method="POST" >
            <% 
 String a = (String) session.getAttribute("user"); 
//String b = (String) session.getAttribute("pass");
 //String c = (String) session.getAttribute("empr");
 //String d = (String) session.getAttribute("depa");

        %>
    <name align="left">Bienvenido: <%=a%> </name>
    <br>
        <table align="right">
            <tr> 
                <td colspan="2" align="right"> <input  type="submit" name="btnlogout" value="Cerrar sesion" class="btn btn-primary"></td>
            </tr>
        </table>
        <br><br>
    </form>
   
    <center><h1>Activos</h1></center>
    <br><br>
        <form action="Controller" method="POST" >
            <table align="center"> 
                <tr>
                    <td colspan="5" align="right"><input type="submit" name="btnagregar" value="Agregar Activo " class="btn btn-primary"></td>
                </tr>
                <tr>
                    <td><br></td>
                </tr>
                  <tr>
                    <td colspan="5" align="right"><input type="submit" name="btneliminar" value="Eliminar Activo " class="btn btn-primary"></td>
                </tr>
                 <tr>
                    <td><br></td>
                </tr>
                 <tr>
                    <td colspan="5" align="right"><input type="submit" name="btnmodificar" value="Modificar Activo" class="btn btn-primary"></td>
                </tr>
                </table>
        </form>
    </body>
</html>
