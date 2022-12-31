const tableBody = document.getElementById('dataTable')

async function getClientes() {
    
    // Peticion HTTP hacia nuestro backend
    let rawResponse = await fetch("http://localhost:3000/cliente", {
        method: "GET",
        headers: { 'Content-type': 'application/json'}
    })
    const response = await rawResponse.json()
    if(rawResponse.status != 200){
         console. log('Hubo un problema cargando la información')
         return
    }
    const {data:clientes}=response;
    limpiarBody()

    clientes.forEach(cliente => {
            const filaNueva = document.createElement('tr')
        	//td class="product-remove"><a href="#"><i class="far fa-window-close"></i></a></td>-->
            const colDPI = document.createElement('td')
            const colNombre = document.createElement('td')
            const colApellido =  document.createElement ('td')
            const colCorreo=document.createElement('td')
            const colEdad = document.createElement('td')
            const colCompras = document.createElement('td')
            const colpassword = document.createElement('td')
            const colAcciones= document.createElement('td')
           const coleditar=document.createElement('td')


           const btneliminar=document.createElement('a')
           const modificar=document.createElement('a')
           const image = document.createElement('img')
           image.src  = 'assets/img/editar.png'

           modificar.appendChild(image)
           coleditar.appendChild(modificar)
           colAcciones.classList.add("product-remove")
           const inconoeliminar = document.createElement('i')
           inconoeliminar.classList.add('far', 'fa-window-close')
           btneliminar.appendChild(inconoeliminar)
           colAcciones.appendChild(btneliminar)


           
            colDPI.innerText =cliente.dpi
            colNombre.innerText = cliente.nombre
            colApellido.innerText = cliente.apellido
            colCorreo.innerText = cliente.correo
            colpassword.innerText=cliente.password
            colEdad.innerText =cliente.edad
            colCompras.innerText= cliente.compras
            
            btneliminar.onclick=() => eliminarcliente(cliente)
           

            filaNueva.appendChild(colDPI)
            filaNueva.appendChild(colCorreo) 
            filaNueva. appendChild(colApellido)
            filaNueva.appendChild(colNombre)
            filaNueva.appendChild(colpassword)
            filaNueva.appendChild(colEdad) 
            filaNueva.appendChild(colCompras)
            filaNueva.appendChild(colAcciones)
            filaNueva.appendChild(coleditar)
            

            tableBody.appendChild(filaNueva)
    });
}
function limpiarBody(){
        while(tableBody.firstChild){
            tableBody.removeChild(tableBody.firstChild)
        }


}
async function eliminarcliente(cliente){
   
    let rawResponse = await fetch("http://localhost:3000/cliente", {
        method: "DELETE",
        headers: { 'Content-type': 'application/json'},
        body: JSON.stringify({

            "dpi": cliente.dpi
          

            })
    })
    const  response=await rawResponse.json()
    location.reload()
    
    alert(response.mensaje)
}

async function modificarcliente(cliente) {
    const correo= document.getElementById('txtmail');
const pwd = document.getElementById('txtcontra');
const nombre= document.getElementById('txtnombre');
const apellido = document.getElementById('txtapellido');
const edad = document.getElementById('txtedad');
const dpi = document.getElementById('txtdpi');
const compras = document.getElementById('txtcompra');
   console.log(cliente)
   nombre.value = cliente.nombre


}


