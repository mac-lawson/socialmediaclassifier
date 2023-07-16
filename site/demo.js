async function sentiment(data) {
	const response = await fetch(
		"https://api-inference.huggingface.co/models/finiteautomata/bertweet-base-sentiment-analysis",
		{
			headers: { Authorization: "Bearer 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" },
			method: "POST",
			body: JSON.stringify(data),
		}
	);
	const result = await response.json();
	return result;
}



