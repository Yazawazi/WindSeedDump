-- 2.7 Only Thanks @lilmayofuksu

local function peaking()
    xlua.hotfix(
        CS.LLJAGKPPOEH, "CBOIHDDDANF",
        function (self, ...)
            base(self):CBOIHDDDANF(self, 1)
        end
    )
end

local function onError(error)
    CS.UnityEngine.GameObject.Find("/BetaWatermarkCanvas(Clone)/Panel/TxtUID"):GetComponent("Text").text = tostring(error)
end

xpcall(peaking, onError)