d3.csv("nbastats.csv", function (data) {

	var svg = d3.select("body").append("svg").attr("height","100%").attr("width","100%");

	svg.selectAll("rect")
    	.data(data)
      	.enter().append("rect")
                .attr("height",function(d,i){ return d.Player_Name * 5; })
                .attr("width","50")
                .attr("fill","pink")
                .attr("x",function(d,i){ return 60*i.Games; })
                .attr("y",function(d,i){ return 300-(d*15); });

}