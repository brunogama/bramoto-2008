/***
 * Bindings
 * @author: Bruno Gama http://profiles.google.com/bgamap
 * 
 */

$(function() {
	
	$('a[rel="external"]').attr({target:'_blank'});
	
	$('#banner a[href*="bramoto"]').click( function(){ return false;} ).css({'cursor':'default'});
	
	$('#valor-personalizado').setMask();
	$('#form-financiamento').submit(function(){ return false;});
	$('#calcular').click(function() {
		var valor = moeda.desformatar($('#valor-personalizado').val());
		var vmin_hidden = $('#hidden-valor-minimo').val();
		var valorh = $('#hidden-valor').val();
		if (vmin_hidden == -1) {
			alert('É necessário escolher uma moto antes de calcular o financiamento.');
		} else {
			if (valor < vmin_hidden) {
				$('#valor-minimo-sugerido').html('R$ '+moeda.formatar(vmin_hidden));
				$('#valor-personalizado').parent().addClass('error');
				$('.to_hide').addClass('hidden');	
			}
			if (valor > vmin_hidden && valor < valorh) {
				$('li.error').removeClass('error');
				$('.to_hide').removeClass('hidden');
				$('#valor-proposto').html('R$ ' + moeda.formatar(valor) );
				var parcelap = ((valorh - (valor))+400)*0.03324;
				$('#valor-prestacao-proposta').html('R$ ' + moeda.formatar(parcelap) );
			}
			if (valor >= valorh) {
				alert('O valor é igual ou excede o valor da moto.');
			}
		}
		return false;
	});
	$('.moto_select').change(function() {
		var preco_moto = parseFloat($(this).val());
	 	$("#preco-moto").html("R$ "+moeda.formatar( preco_moto ) );
		$('#hidden-valor').val( preco_moto );
		var vmin = preco_moto*0.1;
		$("#hidden-valor-minimo").val(vmin);
		vmin = roundNumber(vmin,2);
		vmin = ""+vmin;
		var parcela = ((preco_moto - (preco_moto*0.1))+400)*0.03476;
		parcela = roundNumber(parcela,2);
		parcela = ""+parcela+"";
		$("#valor-minimo").html("R$ "+moeda.formatar(vmin));
		$("#valor-prestacao-minima").html("R$ "+moeda.formatar(parcela));
	});

});