function formatTimeStamp(objDate)
{
	var strMonth = objDate.getMonth() + 1;
	var strDay = objDate.getDate();
	var strYear = objDate.getFullYear();
	var strHour = objDate.getHours();
	var strMinutes = objDate.getMinutes();
	
	var strDate = strMonth+"/" + strDay + "/" + strYear;
	var strTime = strHour + ":" + strMinutes;
	
	return strDate + " " + strTime;
}

function reportSuccess(strMessage)
{
	var divErrors = document.getElementById("divAlert");
	divErrors.innerHTML = strMessage;
	divErrors.className = "alert alert-success";	
}

function reportError(strMessage)
{
	var divErrors = document.getElementById("divAlert");
	divErrors.innerHTML = strMessage;
	divErrors.className = "alert alert-danger";	
}

