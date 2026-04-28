/**
 * Forms Management System
 * Handles async form submissions and UI transitions
 */

document.addEventListener('DOMContentLoaded', () => {
    // 1. Form Signature (DSA - index-data-savings.html)
    const declarationForm = document.getElementById('sign-form');
    if (declarationForm) {
        declarationForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const submitBtn = document.getElementById('sign-btn');
            const webhookUrl = window.APP_CONFIG?.webhooks?.dsaDeclaration;
            
            if (!webhookUrl || webhookUrl === "SUA_NOVA_URL_AQUI") {
                return console.error('DSA Declaration Webhook URL not configured');
            }
            
            const success = await handleFormSubmission(declarationForm, submitBtn, webhookUrl);
            
            if (success) {
                const successDiv = document.getElementById('sign-success');
                if (successDiv) successDiv.classList.add('on');
            }
        });
    }

    // 2. Form Signature (DSA - index-dsa.html)
    const signForm = document.getElementById('signForm');
    if (signForm) {
        signForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const submitBtn = document.getElementById('submitSign');
            const webhookUrl = window.APP_CONFIG?.webhooks?.dsaSign;
            
            if (!webhookUrl) return console.error('DSA Sign Webhook URL not found');
            
            const success = await handleFormSubmission(signForm, submitBtn, webhookUrl);
            
            if (success) {
                const step1 = document.getElementById('signStep1');
                const step2 = document.getElementById('signStep2');
                if (step1) step1.style.display = 'none';
                if (step2) step2.style.display = 'block';
            }
        });
    }

    // 3. Cosponsor Form (DSA)
    const cosponsorForm = document.querySelector('.act-cosponsor-form');
    if (cosponsorForm) {
        cosponsorForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const submitBtn = document.getElementById('submitCosponsor');
            const webhookUrl = window.APP_CONFIG?.webhooks?.dsaCosponsor;

            if (!webhookUrl) return console.error('DSA Cosponsor Webhook URL not found');

            const success = await handleFormSubmission(cosponsorForm, submitBtn, webhookUrl);

            if (success) {
                const step1 = document.getElementById('cosponsorStep1');
                const step2 = document.getElementById('cosponsorStep2');
                if (step1) step1.style.display = 'none';
                if (step2) step2.style.display = 'block';
            }
        });
    }

    // 4. IDR Email Capture
    const idrForm = document.getElementById('idrEmailForm');
    if (idrForm) {
        idrForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const submitBtn = idrForm.querySelector('button[type="submit"]');
            const webhookUrl = window.APP_CONFIG?.webhooks?.idrEmail;

            if (!webhookUrl) return console.error('IDR Email Webhook URL not found');

            await handleFormSubmission(idrForm, submitBtn, webhookUrl);
        });
    }
});

/**
 * Generic handler for Google Apps Script Webhooks
 */
async function handleFormSubmission(form, button, url) {
    const originalBtnText = button.innerHTML;
    
    try {
        button.disabled = true;
        button.innerHTML = 'Sending...';
        
        // IMPORTANT: For Google Apps Script, using URLSearchParams (application/x-www-form-urlencoded)
        // is more reliable than JSON when using 'no-cors' mode.
        const formData = new FormData(form);
        const params = new URLSearchParams();
        
        for (const [key, value] of formData.entries()) {
            params.append(key, value);
        }
        
        await fetch(url, {
            method: 'POST',
            mode: 'no-cors', 
            cache: 'no-cache',
            body: params // Browser will set content-type to application/x-www-form-urlencoded
        });

        // UI Feedback
        button.innerHTML = 'Success!';
        button.style.backgroundColor = '#4CAF50';
        button.style.color = 'white';
        
        setTimeout(() => {
            button.disabled = false;
            button.innerHTML = originalBtnText;
            button.style.backgroundColor = '';
            button.style.color = '';
            form.reset();
        }, 2000);

        return true;

    } catch (error) {
        console.error('Submission error:', error);
        button.innerHTML = 'Error. Try again.';
        button.style.backgroundColor = '#f44336';
        
        setTimeout(() => {
            button.disabled = false;
            button.innerHTML = originalBtnText;
            button.style.backgroundColor = '';
        }, 3000);
        
        return false;
    }
}
