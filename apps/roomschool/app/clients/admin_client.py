import httpx


class AdminPanelClient:
    def __init__(self):
        self.base_url = "http://admin-panel:8000/api"

    async def send_callback(self, payload: dict) -> dict:
        async with httpx.AsyncClient() as client:
            r = await client.post(f"{self.base_url}/callbacks/", json=payload)
            r.raise_for_status()
            return {"message": True}
            # return r.json()


admin_client = AdminPanelClient()
