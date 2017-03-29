<%-- 
    Document   : activoe
    Created on : 26/03/2017, 06:36:16 PM
    Author     : dell
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Eliminar Activo</title>
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
   
    <center><h1>Activos</h1></center>
    <br>
    <center><h4>
        Id del producto
        </h4>   <% 
 String ids = (String) session.getAttribute("idacti"); 
        %>
        
        <applet id="app"
                code="getsome.class"
                ></applet>
        <script type="text/javascript">
            function feedtext(){
                var x = document.getElementById("dropdown1").value;
                
            // app.dosomething(x);
                document.getElementById("descel").innerHTML= "";
                
            }
            
        </script>
    
<% 
    String [] fill = (String[])session.getAttribute("stringarray");
    String ss="";
    for(int i=0;i<fill.length;i++) {
          ss+= "<option>"+fill[i]+"</option>";
} 
 System.out.println(ss);
 
        %>
        
              <select name="dropdown1" id="dropdown1" onchange="feedtext()">
                     <%=ss%>     
        </select>
     <input  type="submit" name="refresel" value="Refresh" class="btn btn-primary">
     
    </center>
    <br>
     <% 
 String name = (String) session.getAttribute("nomeli"); 
        %>
     <center><h4><%=name%></h4></center>
   
        <table align="center">
            <tr> 
  
                <td colspan="2" align="center" placeholder="Username"> 
                      <% 
 String texts = (String) session.getAttribute("desceli"); 
        %>
       <textarea name="descel" rows="4" cols="50" id="descel">
<%=texts%>
</textarea></td>
            </tr>
            <tr> 
                  <td colspan="2" align="center"> <input  type="submit" name="btneliminaract" value="Eliminar Activo" class="btn btn-primary"></td>
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
