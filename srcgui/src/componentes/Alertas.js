import Swal from'sweetalert2';

export default class alerta{
    constructor() { }
    
    mostrar () {Swal.fire({
        position: 'top-end',
        icon: 'success',
        title: 'Your work has been saved',
        showConfirmButton: false,
        timer: 1500
      })}
    }