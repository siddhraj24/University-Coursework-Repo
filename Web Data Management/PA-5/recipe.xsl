<xsl:stylesheet version="2.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<xsl:template match="/">
		<html xmlns="http://www.w3.org/1999/xhtml">
			<body>
				<center><h1 style="background: #121FCF;
background: radial-gradient(ellipse farthest-corner at center center, #121FCF 0%, #CF1512 100%);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
">
					<xsl:value-of select="//collection/description" />
				</h1></center>
				
				<xsl:for-each select="//recipe">
				<div style="box-shadow: 3px 3px 2px 0px rgba(47, 0, 0, 1);">	

						<legend>
							<h2>
								<xsl:value-of select="title" />
							</h2>
						</legend>

						<u><strong>Date: </strong></u>
						<xsl:value-of select="date" />
						<br />
						<br />
						<u><strong>Ingredients:</strong></u>
						<br />
						<ul>
							<xsl:for-each select="ingredient">
								<li>
									<xsl:value-of select="@name" />
									<xsl:if test="@amount">
										<xsl:text> - </xsl:text>
										<xsl:value-of select="@amount" />
									</xsl:if>
									<xsl:if test="@unit">
										<xsl:text> </xsl:text>
										<xsl:value-of select="@unit" />
									</xsl:if>
								</li>
							</xsl:for-each>
						</ul>
						<br />
						<u><strong>Preparation:</strong></u>
						<br />
						<ol>
							<xsl:for-each select="preparation/step">
								<li>
									<xsl:value-of select="." />
								</li>
							</xsl:for-each>
						</ol>
						<xsl:if test="comment">
							<u><strong>Comment:</strong></u>
							<br />
							<xsl:value-of select="comment" />
							<br />
							<br />
						</xsl:if>
						<strong><u>Nutrition: </u></strong>
						<xsl:if test="nutrition/@calories">
							<xsl:text>Calories: </xsl:text>
							<xsl:value-of select="nutrition/@calories" />
							<xsl:text>, </xsl:text>
						</xsl:if>
						<xsl:if test="nutrition/@fat">
							<xsl:text>Fat: </xsl:text>
							<xsl:value-of select="nutrition/@fat" />
							<xsl:text>, </xsl:text>
						</xsl:if>
						<xsl:if test="nutrition/@carbohydrates">
							<xsl:text>Carbohydrates: </xsl:text>
							<xsl:value-of select="nutrition/@carbohydrates" />
							<xsl:text>, </xsl:text>
						</xsl:if>
						<xsl:if test="nutrition/@protein">
							<xsl:text>Protein: </xsl:text>
							<xsl:value-of select="nutrition/@protein" />
						</xsl:if>
						<xsl:if test="nutrition/@alcohol">
							<xsl:text>, Alcohol: </xsl:text>
							<xsl:value-of select="nutrition/@alcohol" />
						</xsl:if>

						<br />
					</div>
				</xsl:for-each>
				
			</body>
		</html>
	</xsl:template>
</xsl:stylesheet>
