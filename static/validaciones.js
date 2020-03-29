function validar_paciente()
{
    var nombre_paciente, rut_paciente, fecha_nacimiento;
    nombre_paciente= document.getElementById("nombrePaciente").value; 
    rut_paciente= document.getElementById("rutPaciente").value;
    fecha_nacimiento= document.getElementById("fechaNacimiento").value;

    if(nombre_paciente==="")
    {
        alert("El nombre del paciente NO ha sido ingresado.");
        return false; 
    }
        else if(rut_paciente==="")
        {
            alert("El rut del paciente NO ha sido ingresado.");
            return false;
        }
        else if(fecha_nacimiento==="")
        {
            alert("La fecha de nacimiento del paciente NO ha sido ingresada.");
            return false; 
        }
    else
    {
        alert("Paciente registrado exitosamente!");
        return true; 
    }
}

function validar_vacuna()
{
    var nombre_enfermedad;
    nombre_enfermedad= document.getElementById("nombreEnfermedad").value;

    if(nombre_enfermedad==="")
    {
        alert("El nombre de la enfermedad NO ha sido ingresado.");
        return false; 
    }
    else
    {
        alert("Vacuna registrada exitosamente!");
        return true; 
    }
}

function vacunar_paciente()
{
    var vacuna_paciente;
    vacuna_paciente=document.getElementById("vacunaPaciente").value;
    if(vacuna_paciente==0)
    {
      alert("NO se ha seleccionado una vacuna.");
      return false;
    }
    else
    {
      alert("Vacuna ingresada exitosamente !");
      return true;  
    }

}