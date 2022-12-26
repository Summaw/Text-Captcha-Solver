const axios = require('axios');


async function main(captcha_url) {
    var config = {
        method: 'get',
        url: `http://127.0.0.1:5000/?url=${captcha_url}`,
        headers: { }
      };
      
      axios(config)
      .then(function (response) {
        console.log(JSON.stringify(response.data))
        if ( response.status == 200) {
            console.log(`Solved Captcha: ` + response.data.response)
        } else {
            console.log(`[+] Error: ${response.status}`)
        }
      })
      .catch(function (error) {
        console.log(error);
      });
}

main("captchaimage_url");
