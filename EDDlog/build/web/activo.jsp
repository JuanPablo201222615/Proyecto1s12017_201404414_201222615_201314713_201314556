<%-- 
    Document   : activo
    Created on : 26/03/2017, 12:06:41 AM
    Author     : dell
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Crear activo</title>
         <link href="bootstrap.css" type="text/css" rel="stylesheet">
          <style type="text/css">
   body { background: #e6ff99 !important; }
     h1 { background: #ff8566 !important; }/* Adding !important forces the browser to overwrite the default style applied by Bootstrap */
</style>
    </head>
    <body>
   
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
 
   
    <center><h1>Activos</h1> <br>
    Nombre: <input type="text" name="txtnombreact" placeholder="Ingrese nombre"></center>
    <br><br>
    
         <% 
 String name = (String) session.getAttribute("nombreactivo"); 
        %>
     <center><h4><%=name%></h4></center>
   
        <table align="center">
            <tr> 
                <td colspan="2" align="center" placeholder="Username"> <textarea name="description" rows="4" cols="50">
</textarea></td>
            </tr>
            <tr> 
                  <td colspan="2" align="center"> <input  type="submit" name="btnagregaract" value="Agregar Activo" class="btn btn-primary"></td>
            </tr>
            <tr><td>
                    <br>
                </td></tr>
              <tr> 
                  <td colspan="2" align="center"> <input  type="submit" name="btnreturn2" value="Retornar" class="btn btn-primary"></td>
            </tr>
        </table>
        </form>
    
      </body>
</html>
