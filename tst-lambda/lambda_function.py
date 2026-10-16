import json
import os

def lambda_handler(event, context):
    # Pega das variáveis de ambiente do template.yaml
    env = os.getenv("ENV", "desconhecido")
    bucket = os.getenv("BUCKET_NAME", "sem-bucket")

    nome = "DevOps"
    
    # URL ?name=...
    params = event.get("queryStringParameters")
    if params and params.get("name"):
        nome = params.get("name")
    
    # Body JSON {"name": "..."}
    body = event.get("body")
    if body:
        try:
            data = json.loads(body)
            if data.get("name"):
                nome = data.get("name")
        except:
            pass

    # LOG - aparece no terminal do sam local
    print(f"[LOG] Ambiente: {env} | Bucket: {bucket} | Nome recebido: {nome}")

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({
            "message": f"Agora sou {nome}!!!",
            "ambiente": env,
            "bucket_configurado": bucket,
            "metodo": event.get("httpMethod"),
            "status": "projeto finalizado com sucesso"
        })
    }