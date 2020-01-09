select_factores = document.getElementById("factores");
select_caracteristicas = document.getElementById("caracteristicas");
tbody_objetivos = document.getElementById("tbody_objetivos")
objetivoSeleccionado = document.getElementById("objetivoSeleccionado");


/* Registro de eventos */
select_factores.addEventListener("change", cargarCaracteristicas)
select_caracteristicas.addEventListener("change", cargarObjetivos)
/* Fin Registro de eventos */


function relacionarObjetivo(event){
    objetivoSeleccionado.innerHTML = '';

    //alert(event);
    console.log(event.cells.item(0).innerHTML);
   // alert(event.cells.item(1).innerText);

    if (event.cells.item(1).innerText!=undefined){

        let texto = "Objetivo: "
        texto += event.cells.item(1).innerText;
        //alert(texto);
        
        let nodotexto = document.createTextNode(texto);
        
        //nodotexto.setAttribute("style", "border: 1px solid green");
       // nodotexto.style.borderStyle = "solid";
                
        objetivoSeleccionado.appendChild(nodotexto);
        
        /* var evtType = event.type
        alert(evtType)*/
    }
       
}

function cargarObjetivos(){

    let caracterisSeleccionada = select_caracteristicas.value;
    console.log(caracterisSeleccionada);

    fetch("cargarobjetivos/"+caracterisSeleccionada)
    .then( (response)=>{
        return response.json()
    })
    .then((data)=>{
        console.log(data)
       
        document.querySelectorAll('#tbody_objetivos tr').forEach(fila => fila.remove())

        for (let i = 0; i < data.length; i++) {
          fila = document.createElement('tr');
          columna1 = document.createElement('td');
          columna2 = document.createElement('td');
          parrafo = document.createElement('p');
          
          link = document.createElement('a');
          link.text = data[i].descripcion;
          //link.setAttribute("href", "#");
          
          
          parrafo.appendChild(link);
          parrafo.setAttribute("style", "text-align:justify");
          columna2.appendChild(parrafo);

          textoIdObjetivo = document.createTextNode(data[i].id)
          columna1.appendChild(textoIdObjetivo);
          columna1.setAttribute("style", "display:none");

          fila.appendChild(columna1);
          fila.appendChild(columna2);
          fila.setAttribute("onClick", "relacionarObjetivo(this)");



          tbody_objetivos.appendChild(fila);

    	}    
    })
    .catch(function(error) {
        console.log('dentro de cargar objetivos Hubo un problema con la petición Fetch:' + error.message);
        document.querySelectorAll('#tbody_objetivos tr').forEach(fila => fila.remove())
      });
 


}

function cargarCaracteristicas(){

    let factorSeleccionado = select_factores.value;
    console.log(factorSeleccionado);

    fetch("cargarcaracteristicas/"+factorSeleccionado)
    .then( (response)=>{
        return response.json()
    })
    .then((data)=>{
        console.log(data)


        
        document.querySelectorAll('#caracteristicas option').forEach(option => option.remove())

        let option;
    
    	for (let i = 0; i < data.length; i++) {
          option = document.createElement('option');
      	  option.text = data[i].descripcion;
      	  option.value = data[i].id;
      	  select_caracteristicas.add(option);
        }  
        
        if (data.length>0)
        {
           cargarObjetivos();
        }else{
            document.querySelectorAll('#tbody_objetivos tr').forEach(fila => fila.remove());
        }
    })
    .catch(function(error) {
        console.log('Hubo un problema con la petición Fetch:' + error.message);
        document.querySelectorAll('#caracteristicas option').forEach(option => option.remove())
        document.querySelectorAll('#tbody_objetivos tr').forEach(fila => fila.remove())
      });
}



