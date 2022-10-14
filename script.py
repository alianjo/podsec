import kopf

@kopf.on.update('', 'v1', 'pod')
def on_create(name, namespace, spec, body, **kwargs):
    for i in body['spec']['containers']:
        securityContext = i.get("securityContext")
        if securityContext is None:
            continue
        else:
            if securityContext.get('privileged') == True:
                kopf.warn(body, reason='Security', message='running as privilaged container')
                return 
    if body['spec'].get('hostNetwork') == True:
        kopf.warn(body, reason='Security', message='host Network is enabled')
        return 
    if body['spec'].get('hostPID') == True:
        kopf.warn(body, reason='Security', message='host PID is enabled')
        return 
    if body['spec'].get('hostIPC') == True:
        kopf.warn(body, reason='Security', message='host IPC is enabled')
        return 
        
@kopf.on.create('', 'v1', 'pod')
def on_create(name, namespace, spec, body, **kwargs):
    for i in body['spec']['containers']:
        securityContext = i.get("securityContext")
        if securityContext is None:
            continue
        else:
            if securityContext.get('privileged') == True:
                kopf.warn(body, reason='Security', message='running as privilaged container')
                return 
    if body['spec'].get('hostNetwork') == True:
        kopf.warn(body, reason='Security', message='host Network is enabled')
        return 
    if body['spec'].get('hostPID') == True:
        kopf.warn(body, reason='Security', message='host PID is enabled')
        return 
    if body['spec'].get('hostIPC') == True:
        kopf.warn(body, reason='Security', message='host IPC is enabled')
        return 
