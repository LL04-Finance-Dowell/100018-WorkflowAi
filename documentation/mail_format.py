

<<<<<<< HEAD
def formated_mail(email, document_link):
=======
def formated_mail(email, link):
>>>>>>> cb178417b7f102c7144a630b7f129917a7187c02
    return """<link href='https://maxcdn.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css' rel='stylesheet' id='bootstrap-css'>
    <script src='https://maxcdn.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js'></script>
    <script src='https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js'></script>
    <!------ Include the above in your HEAD tag ---------->

    <!DOCTYPE html>
    <html>

    <head>
        <title></title>
        <meta http-equiv='Content-Type' content='text/html; charset=utf-8' />
        <meta name='viewport' content='width=device-width, initial-scale=1'>
        <meta http-equiv='X-UA-Compatible' content='IE=edge' />

        <style type='text/css'>
            @media screen {
                @font-face {
                    font-family: 'Lato';
                    font-style: normal;
                    font-weight: 400;
                    src: local('Lato Regular'), local('Lato-Regular'), url(https://fonts.gstatic.com/s/lato/v11/qIIYRU-oROkIk8vfvxw6QvesZW2xOQ-xsNqO47m55DA.woff) format('woff');
                }

                @font-face {
                    font-family: 'Lato';
                    font-style: normal;
                    font-weight: 700;
                    src: local('Lato Bold'), local('Lato-Bold'), url(https://fonts.gstatic.com/s/lato/v11/qdgUG4U09HnJwhYI-uK18wLUuEpTyoUstqEm5AMlJo4.woff) format('woff');
                }

                @font-face {
                    font-family: 'Lato';
                    font-style: italic;
                    font-weight: 400;
                    src: local('Lato Italic'), local('Lato-Italic'), url(https://fonts.gstatic.com/s/lato/v11/RYyZNoeFgb0l7W3Vu1aSWOvvDin1pK8aKteLpeZ5c0A.woff) format('woff');
                }

                @font-face {
                    font-family: 'Lato';
                    font-style: italic;
                    font-weight: 700;
                    src: local('Lato Bold Italic'), local('Lato-BoldItalic'), url(https://fonts.gstatic.com/s/lato/v11/HkF_qI1x_noxlxhrhMQYELO3LdcAZYWl9Si6vvxL-qU.woff) format('woff');
                }
            }

            /* CLIENT-SPECIFIC STYLES */
            body,
            table,
            td,
            a {
                -webkit-text-size-adjust: 100%;
                -ms-text-size-adjust: 100%;
            }

            table,
            td {
                mso-table-lspace: 0pt;
                mso-table-rspace: 0pt;
            }

            img {
                -ms-interpolation-mode: bicubic;
            }

            /* RESET STYLES */
            img {
                border: 0;
                height: auto;
                line-height: 100%;
                outline: none;
                text-decoration: none;
            }

            table {
                border-collapse: collapse !important;
            }

            body {
                height: 100% !important;
                margin: 0 !important;
                padding: 0 !important;
                width: 100% !important;
            }

            /* iOS BLUE LINKS */
            a[x-apple-data-detectors] {
                color: inherit !important;
                text-decoration: none !important;
                font-size: inherit !important;
                font-family: inherit !important;
                font-weight: inherit !important;
                line-height: inherit !important;
            }

            /* MOBILE STYLES */
            @media screen and (max-width:600px) {
                h1 {
                    font-size: 32px !important;
                    line-height: 32px !important;
                }
            }

            /* ANDROID CENTER FIX */
            div[style*='margin: 16px 0;'] {
                margin: 0 !important;
            }
        </style>
    </head>""" + f"""
    <body style='background-color: #f4f4f4; margin: 0 !important; padding: 0 !important;'>
    <!-- HIDDEN PREHEADER TEXT >
    <div style='display: none; font-size: 1px; color: #fefefe; line-height: 1px; font-family: 'Lato', Helvetica, Arial, sans-serif; max-height: 0px; max-width: 0px; opacity: 0; overflow: hidden;'></div -->
    <table border='0' cellpadding='0' cellspacing='0' width='100%'>
        <!-- LOGO -->
        <tr>
            <td bgcolor='#21633d' align='center'>
                <table border='0' cellpadding='0' cellspacing='0' width='100%' style='max-width: 600px;'>
                    <tr>
                        <td align='center' valign='top' style='padding: 40px 10px 40px 10px;'> </td>
                    </tr>
                </table>
            </td>
        </tr>
        <tr>
            <td bgcolor='#21633d' align='center' style='padding: 0px 10px 0px 10px;'>
                <table border='0' cellpadding='0' cellspacing='0' width='100%' style='max-width: 600px;'>
                    <tr>
                        <td bgcolor='#ffffff' align='center' valign='top' style='padding: 40px 20px 20px 20px; border-radius: 4px 4px 0px 0px; color: #111111; font-family: 'Lato', Helvetica, Arial, sans-serif; font-size: 48px; font-weight: 400; letter-spacing: 4px; line-height: 48px;'>
                            <!-- <h1 style='font-size: 48px; font-weight: 400; margin: 2;'>Don't Leave!</h1> <img src=' https://img.icons8.com/clouds/100/000000/sad.png' width='125' height='120' style='display: block; border: 0px;' /> -->
                             <img src='https://100018.pythonanywhere.com/static/images/doc_logo1.png' width='150' height='150' style='display: block; border: 0px;' /><h2 style=''font-size: 28px; color: #000;  font-weight: 400; margin: 2;'>Signature required</h2>


                        </td>
                    </tr>
                </table>
            </td>
        </tr>
        <tr>
            <td bgcolor='#f4f4f4' align='center' style='padding: 0px 10px 0px 10px;'>
                <table border='0' cellpadding='0' cellspacing='0' width='100%' style='max-width: 600px;'>
                    <tr>
                        <td bgcolor='#ffffff' align='left' style='padding: 20px 30px 40px 30px; color: #666666; font-family: 'Lato', Helvetica, Arial, sans-serif; font-size: 18px; font-weight: 400; line-height: 25px;'>
                            <p style='margin: 0 74px; font-size: 16px; color: #000;' >
                                The document sent by Dowell Research is awaiting your signature.
                                To review and sign the document, please click the button below or
<<<<<<< HEAD
                                <a href={document_link}>
=======
                                <a href={link}>
>>>>>>> cb178417b7f102c7144a630b7f129917a7187c02
                                Click Here</a> <br><br>
                                </p>
                        </td>
                    </tr>
                    <tr>
                        <td bgcolor='#ffffff' align='left'>
                            <table width='100%' border='0' cellspacing='0' cellpadding='0'>
                                <tr>
                                    <td bgcolor='#ffffff' align='center' style='padding: 20px 30px 60px 30px;'>
                                        <table border='0' cellspacing='0' cellpadding='0'>
                                            <tr>
<<<<<<< HEAD
                                                <td align='center' style='border-radius: 3px;' bgcolor='#21633d'><a href={document_link} target='_blank' style='font-size: 20px; font-family: Helvetica, Arial, sans-serif; color: #ffffff; text-decoration: none; color: #fdec00; text-decoration: none; padding: 15px 25px; border-radius: 2px; border: 1px solid #21633d; display: inline-block;'>View Document</a></td>
=======
                                                <td align='center' style='border-radius: 3px;' bgcolor='#21633d'><a href={link} target='_blank' style='font-size: 20px; font-family: Helvetica, Arial, sans-serif; color: #ffffff; text-decoration: none; color: #fdec00; text-decoration: none; padding: 15px 25px; border-radius: 2px; border: 1px solid #21633d; display: inline-block;'>View Document</a></td>
>>>>>>> cb178417b7f102c7144a630b7f129917a7187c02
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>

                    <tr>
                        <td bgcolor='#ffffff' align='left' style='padding: 0px 30px 20px 30px; color: #666666; font-family: 'Lato', Helvetica, Arial, sans-serif; font-size: 18px; font-weight: 400; line-height: 25px;'>
                            <p style='margin: 0 74px; font-size: 16px; color: #000;' >If you have any questions, just reply to this email—we're always happy to help out.</p>
                        </td>
                    </tr>
                    <tr>
                        <td bgcolor='#ffffff' align='left' style='padding: 0px 30px 40px 30px; border-radius: 0px 0px 4px 4px; color: #666666; font-family: 'Lato', Helvetica, Arial, sans-serif; font-size: 18px; font-weight: 400; line-height: 25px;'>
                            <p style='margin: 0 74px; font-size: 16px; color: #000;' > Thank You<br>
                                <br>
                            </p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
        <tr>
            <td bgcolor='#f4f4f4' align='center' style='padding: 30px 10px 0px 10px;'>
                <table border='0' cellpadding='0' cellspacing='0' width='100%' style='max-width: 600px;'>
                    <tr>
                        <td bgcolor='#FFECD1' align='center' style='padding: 30px 30px 30px 30px; border-radius: 4px 4px 4px 4px; color: #666666; font-family: 'Lato', Helvetica, Arial, sans-serif; font-size: 18px; font-weight: 400; line-height: 25px;'>
                            <h2 style='font-size: 20px; font-weight: 400; color: #111111; margin: 0;'>Need more help?</h2>
                            <p style='margin: 0 74px; font-size: 16px; color: #000;'><a href='#' target='_blank' style='color: #21633d;'>We’re here to help you out</a></p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
        <tr>
            <td bgcolor='#f4f4f4' align='center' style='padding: 0px 10px 0px 10px;'>
                <table border='0' cellpadding='0' cellspacing='0' width='100%' style='max-width: 600px;'>
                    <tr>
                        <td bgcolor='#f4f4f4' align='left' style='padding: 0px 30px 30px 30px; color: #666666; font-family: 'Lato', Helvetica, Arial, sans-serif; font-size: 14px; font-weight: 400; line-height: 18px;'> <br>
                            <p style='margin: 0 74px; font-size: 16px; color: #000;' >Copyright message <a href='#' target='_blank' style='color: #111111; font-weight: 700;'>dowell @2022</a>.</p>
                        </td>
                    </tr>
                </table>

            </td>
        </tr>
    </table>
    </body>

    </html>"""




